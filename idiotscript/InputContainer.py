class InputContainer(object):
    EOF='\x00'
    def __init__(self, inputtext):
        self._inputtext = inputtext
        self._pointer = 0
        self._inputlength = len(inputtext)

    def reset(self):
        self._pointer = 0

    @property
    def inputtext(self):
        return self._inputtext

    def get_at_pointer(self):
        if self.iseof():
            return InputContainer.EOF
        return self._inputtext[self._pointer:]

    @property
    def pointer(self):
        return self._pointer

    def move_pointer(self, amount):
        self._pointer += amount

    def iseof(self):
        return self._pointer >= self._inputlength

    def move_to_eof(self):
        self._pointer = self._inputlength
