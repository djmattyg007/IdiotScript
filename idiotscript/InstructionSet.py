def starts_with(str1, str2):
    if str1[:len(str2)] == str2:
        return True
    else:
        return False

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
        for name, klass in self.instructions.items():
            if len(search_string) < len(klass.INSTRUCTION):
                continue
            if starts_with(search_string, klass.INSTRUCTION):
                if len(search_string) == len(klass.INSTRUCTION) or search_string[len(klass.INSTRUCTION)] == " ":
                    return klass(search_string)
        return None

