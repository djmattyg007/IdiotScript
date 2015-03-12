class InstructionList(object):
    '''
    An instruction list is the result of parsing an
    idiotscript script. It may have nested instruction
    lists, which is the result of branching in the
    idiotscript. This implementation uses a linked list.
    '''
    def __init__(self):
        self._head = None
        self._tail = None
        self._current = None

    def isempty(self):
        return self._head == None

    def add(self, instruction, branch = None):
        new_node = self.Node(instruction, branch)
        if self.isempty() == True:
            self._head = new_node
        else:
            self._tail.successor = new_node
        self._tail = new_node

    def __str__(self):
        return InstructionList.str_ilist(self)

    @staticmethod
    def str_ilist(ilist, depth = 0):
        '''
        Pretty-prints an instruction list, representing branches
        with indented lines.
        '''
        temp = ""
        for instruction, branch in ilist:
            temp += "  " * depth
            temp += str(instruction) + "\n"
            if branch is not None:
                temp += InstructionList.str_ilist(branch, depth + 1)
        return temp

    def __iter__(self):
        self.reset()
        return self

    def __next__(self):
        '''
        Returns a tuple containing the current instruction,
        and a nested instruction list (the branch) if it is
        a branching instruction.
        '''
        if self._current is None:
            raise StopIteration
        instruction = self._current.instruction
        branch = self._current.branch
        self._current = self._current.successor
        return (instruction, branch)

    def reset(self):
        '''
        In order to support the "repeat" instruction, it
        is necessary to be able to manually reset the iterator
        back to the start of the instruction list.
        '''
        self._current = self._head

    class Node(object):
        def __init__(self, instruction, branch = None):
            self._instruction = instruction
            self._branch = branch
            self._successor = None

        @property
        def instruction(self):
            return self._instruction

        @property
        def successor(self):
            return self._successor

        @successor.setter
        def successor(self, successor):
            self._successor = successor

        @property
        def branch(self):
            return self._branch

        @branch.setter
        def branch(self, ilist):
            self._branch = ilist
