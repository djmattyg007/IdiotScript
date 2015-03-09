class InstructionBase(object):
    BEFORE=None
    AFTER=None

    def __init__(self, search_string):
        self.search_string = search_string

    @property
    def search_string(self):
        return self._search_string

    @search_string.setter
    def search_string(self, value):
        if value.startswith(self.INSTRUCTION):
            temp = value[(len(self.INSTRUCTION) + 1):]
        else:
            temp = value
        self._search_string = temp.replace("\\n", "\n")

    def __str__(self):
        return self.INSTRUCTION + " " + self.search_string

    def run(self, inputcontainer):
        return (None, False)

    def _search(self, inputcontainer):
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
            inputcontainer.move_to_eof()
        else:
            inputcontainer.move_pointer(offset)
            text = text[:offset]
        return text

    def _if(self, inputcontainer):
        text = inputcontainer.get_at_pointer()
        if text.startswith(self.search_string):
            return True
        else:
            return False
