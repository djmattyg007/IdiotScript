class InstructionBase(object):
    # If BEFORE is set to "branch", this means this instruction is
    # used to terminate a nested branch (typically elseif/else/endif).
    BEFORE=None
    # If AFTER is set to "branch", this means this instruction is
    # used to commence a nested branch (typically if/elseif/else).
    AFTER=None

    def __init__(self, search_string):
        self.search_string = search_string

    @property
    def search_string(self):
        return self._search_string

    @search_string.setter
    def search_string(self, value):
        if value.startswith(self.INSTRUCTION):
            # Strip off the instruction's command, plus the
            # space directly after the command, leaving behind
            # just the parameter passed to the command. This
            # is treated as the search string, because in the
            # default instruction set, it is primarily used for
            # searching through the input text.
            temp = value[(len(self.INSTRUCTION) + 1):]
        else:
            # Support, for whatever reason, search strings
            # that don't start with the instruction's command.
            temp = value
        self._search_string = temp.replace("\\n", "\n")

    def __str__(self):
        return self.INSTRUCTION + " " + self.search_string

    def run(self, inputcontainer):
        '''
        The first return parameter is text to be saved into the
        collector. The second return parameter is whether or not
        the script runner should follow this instruction's nested
        branch.
        '''
        return (None, False)

    def _search(self, inputcontainer):
        '''
        Helper method for searching through the text at the current
        position of the input container. This is used for searching
        and copying the text in the input container.
        '''
        text = inputcontainer.get_at_pointer()
        if text == inputcontainer.EOF:
            return inputcontainer.EOF
        offset = text.find(self.search_string)
        if offset == -1:
            return inputcontainer.EOF
        else:
            return offset

    def _copy(self, inputcontainer):
        text = inputcontainer.get_at_pointer()
        offset = self._search(inputcontainer)
        if offset == inputcontainer.EOF:
            # If we can't find the specified text, move the input
            # container's pointer to the end of the input text.
            inputcontainer.move_to_eof()
        else:
            # If we can find the specified text, move the pointer
            # to the start of the specified text, and copy everything
            # from where we started to where we are now.
            inputcontainer.move_pointer(offset)
            text = text[:offset]
        return text

    def _if(self, inputcontainer):
        text = inputcontainer.get_at_pointer()
        if text.startswith(self.search_string):
            return True
        else:
            return False
