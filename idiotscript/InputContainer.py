class InputContainer(object):
    '''
    The input container's EOF constant should be used by
    other code to signal that the end of the input has
    been reached, and that processing should terminate
    immediately. Implementations should not depend on the
    EOF constant being any particular value.
    '''
    EOF='\x00'

    def __init__(self, inputtext):
        '''
        inputtext could be any object that acts like an array of
        characters. It's recommended to use a string with this
        implementation though.
        '''
        self._inputtext = inputtext
        self._pointer = 0
        self._inputlength = len(inputtext)

    def reset(self):
        self._pointer = 0

    @property
    def inputtext(self):
        return self._inputtext

    def get_at_pointer(self):
        '''
        Returns all text from the position of the pointer to the
        end of the string, or the EOF constant if the pointer
        has been advanced past the endpoint of the array of
        characters.
        '''
        if self.iseof():
            return InputContainer.EOF
        return self._inputtext[self._pointer:]

    @property
    def pointer(self):
        return self._pointer

    def move_pointer(self, amount):
        '''
        Move the pointer forwards or backwards by the given amount.
        Typically this will just be used to move it forwards, but
        there's nothing stopping someone from creating their own
        instructions that move the pointer backwards for whatever
        reason.
        '''
        self._pointer += amount

    def iseof(self):
        return self._pointer >= self._inputlength

    def move_to_eof(self):
        self._pointer = self._inputlength
