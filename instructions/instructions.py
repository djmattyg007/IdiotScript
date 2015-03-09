from .base import InstructionBase

class SearchPastInstruction(InstructionBase):
    INSTRUCTION="search past"
    def run(self, inputcontainer):
        offset = self._search(inputcontainer)
        if offset == inputcontainer.EOF:
            return (inputcontainer.EOF, False)
        else:
            inputcontainer.move_pointer(offset + len(self.search_string))
            return (None, False)

class SearchUpTillInstruction(InstructionBase):
    INSTRUCTION="search up till"
    def run(self, inputcontainer):
        offset = self._search(inputcontainer)
        if offset == inputcontainer.EOF:
            return (inputcontainer.EOF, False)
        else:
            inputcontainer.move_pointer(offset)
            return (None, False)

class CopyTillWithInstruction(InstructionBase):
    INSTRUCTION="copy till with"
    def run(self, inputcontainer):
        text = self._copy(inputcontainer)
        if not inputcontainer.iseof():
            inputcontainer.move_pointer(len(self.search_string))
            text += self.search_string
        return (text, False)

class CopyUpTillInstruction(InstructionBase):
    INSTRUCTION="copy up till"
    def run(self, inputcontainer):
        return (self._copy(inputcontainer), False)

class IfInstruction(InstructionBase):
    INSTRUCTION="if you find"
    AFTER="branch"
    def run(self, inputcontainer):
        return (None, self._if(inputcontainer))

class ElseIfInstruction(InstructionBase):
    INSTRUCTION="or if you find"
    BEFORE="branch"
    AFTER="branch"
    def run(self, inputcontainer):
        return (None, self._if(inputcontainer))

class ElseInstruction(InstructionBase):
    INSTRUCTION="otherwise"
    BEFORE="branch"
    AFTER="branch"
    def run(self, inputcontainer):
        return (None, True)

class EndIfInstruction(InstructionBase):
    INSTRUCTION="then"
    BEFORE="branch"

class RepeatInstruction(InstructionBase):
    INSTRUCTION="repeat"
    AFTER="restart"

