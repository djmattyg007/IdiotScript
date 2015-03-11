class ScriptRunner(object):
    def __init__(self, inputcontainer):
        self._inputcontainer = inputcontainer

    def run(self, ilist, collector):
        self._inputcontainer.reset()
        self._run(ilist, collector)

    def _run(self, ilist, collector, depth = 0):
        ilist.reset()
        for instruction, branch in ilist:
            result = None
            (text, should_branch) = instruction.run(self._inputcontainer)
            if text == self._inputcontainer.EOF:
                return self._inputcontainer.EOF
            elif text != None:
                collector.add_input(text)
            if should_branch:
                result = self._run(branch, collector, depth + 1)
                if result == self._inputcontainer.EOF:
                    return self._inputcontainer.EOF
                elif result == True:
                    # Cycle past all the other remaining branches on this level
                    (extra_instruction, extra_branch) = ilist.__next__()
                    while extra_instruction.AFTER == "branch":
                        (extra_instruction, extra_branch) = ilist.__next__()
            if "restart" in [instruction.AFTER, result]:
                ilist.reset()
                collector.new_group()
                if depth > 0:
                    return "restart"
        return True
