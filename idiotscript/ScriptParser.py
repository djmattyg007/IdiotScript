class ScriptParser(object):
    '''
    Given an instruction set, a factory for instruction
    lists, and a script, this class will parse any idiotscript
    script into a nested instruction list for use with the
    script runner.
    '''
    def __init__(self, iset, ilist_factory):
        '''
        We require a factory for the instruction list class
        because we don't know how many of these we're going
        to need. The idiotscript module provides a factory
        for the default implementation.
        '''
        self._iset = iset
        self._ilist_factory = ilist_factory

    def parse(self, script):
        '''
        Prefer an array of strings, but if we get passed a
        string, turn it into an array of strings.
        '''
        if type(script) is str:
            _script = script.splitlines()
        else:
            _script = script
        return self._parse(_script)

    def _parse(self, script):
        '''
        Create a stack to store instructions and instruction lists
        when parsing branching instructions. A stack is used
        because we can infinitely nest branches in this
        implementation.
        '''
        istack = stack()
        cur_ilist = self._ilist_factory()
        for line in script:
            instruction = self._iset.match_string(line)
            if instruction is None:
                continue

            if instruction.BEFORE == "branch":
                '''
                If this instruction represents the end of a branch
                (typically elseif/else/endif), we need to finish
                processing the previous branch first.
                '''
                # Save the current instruction list, as this is the
                # branch being saved underneath its open branch
                # instruction.
                branch = cur_ilist
                # Retrieve the open branch instruction, and the original
                # instruction list that the open branch instruction belongs
                # on.
                (parent, cur_ilist) = istack.pop()
                # Store the open branch instruction with its nested branch
                # instruction list on the original instruction list.
                cur_ilist.add(parent, branch)
            if instruction.AFTER == "branch":
                '''
                If this is a branching instruction (typically
                if/elseif/else), push the current instruction,
                and the current instruction list, onto a stack.
                It will be retrieved later, when the next branching
                instruction is reached (elseif/else), or the end
                of the branch is reached (endif).
                '''
                istack.push((instruction, cur_ilist))
                cur_ilist = self._ilist_factory()
            else:
                cur_ilist.add(instruction)
        return cur_ilist

class stack(list):
    '''
    Convenience wrapper to make a list behave like
    a traditional stack with push/pop operations.
    '''
    def push(self, item):
        self.append(item)
