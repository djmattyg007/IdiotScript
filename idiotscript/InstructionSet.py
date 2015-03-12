class InstructionSet(object):
    def __init__(self):
        self.instructions = {}

    def add(self, name, klass):
        self.instructions[name] = klass
        return self

    def remove(self, name):
        self.instructions.pop(name)
        return self

    def match_string(self, search_string):
        '''
        search_string should be a line from the script being
        run (both the instruction and any text after it). The
        instructions in the set are iterated over one by one,
        trying to match the start of the line with the command
        that represents the instruction.

        When it finds an instruction with a matching command,
        it makes sure that there is a trailing space after the
        command in the search string (representing the gap
        between the command and the parameter to the comamnd),
        or that the line is exactly the same length as the
        command (in the case of instructions such as else
        (represented by "otherwise") which do not take parameters.

        Once this check has been passed, it creates an instance
        of the class that represents that instruction and sends
        it back to the caller.
        '''
        for name, klass in self.instructions.items():
            if len(search_string) < len(klass.INSTRUCTION):
                continue
            if search_string.startswith(klass.INSTRUCTION):
                if len(search_string) == len(klass.INSTRUCTION) or search_string[len(klass.INSTRUCTION)] == " ":
                    return klass(search_string)
        return None

