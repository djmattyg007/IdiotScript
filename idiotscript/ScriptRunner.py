class ScriptRunner(object):
    '''
    Take an input container, an instruction list, and a collector,
    and store the text parsed out of the input text in the collector
    using the instructions in the instruction list.
    '''
    def __init__(self, inputcontainer):
        self._inputcontainer = inputcontainer

    def run(self, ilist, collector):
        self._inputcontainer.reset()
        self._run(ilist, collector)

    def _run(self, ilist, collector, depth = 0):
        # Always reset the instruction list's iterator, in case this isn't
        # the first time we're iterating over it. We always want to start
        # iterating over an instruction list from the beginning.
        ilist.reset()

        # Not every instruction will have a child instruction list branch,
        # but it's much easier to always grab it even if it's None
        for instruction, branch in ilist:
            result = None
            # The first step is always to run the current instruction.
            # There isn't a situation where this shouldn't occur.
            # There should always be two components in the return value
            # of the instruction. Even if the instruction is an if/elseif
            # instruction, we still can't be sure if we need to branch, in
            # case the if test fails.
            (text, should_branch) = instruction.run(self._inputcontainer)
            if text == self._inputcontainer.EOF:
                # If we reached the end of the file, end immediately,
                # ensuring this is propogated up the stack.
                return self._inputcontainer.EOF
            elif text != None:
                # If we didn't reach the end of the file, and we did get
                # some text from the instruction (probably from a copy
                # instruction), save it in the collector.
                collector.add_input(text)
            if should_branch:
                # If an if/elseif/else instruction was successful, delve into
                # the child branch. Run all instructions in the child branch.
                result = self._run(branch, collector, depth + 1)
                if result == self._inputcontainer.EOF:
                    # Again, if we reached the end of the file as a result
                    # of delving into this branch, end immediately.
                    return self._inputcontainer.EOF
                elif result == True:
                    # If the branch completed successfully (all instrctions were
                    # run and we didn't reach the end of the file), cycle past
                    # all the other remaining branches on this level. For example,
                    # if the if branch was executed, and there's an else branch,
                    # we need to cycle past this else branch.
                    (extra_instruction, extra_branch) = ilist.__next__()
                    while extra_instruction.AFTER == "branch":
                        (extra_instruction, extra_branch) = ilist.__next__()
            if "restart" in [instruction.AFTER, result]:
                # Tecnically, the "repeat" instruction can appear
                # anywhere in a script, not just at the end. Therefore,
                # we need to support this possibility. Either we're on
                # the top-level branch (no nesting), or we were in a
                # nested branch and have moved up a nesting level.
                ilist.reset()
                collector.new_group()
                if depth > 0:
                    return "restart"
        return True
