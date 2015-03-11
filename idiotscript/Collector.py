class Collector(object):
    def __init__(self):
        self._groups = []
        self._current_group = None

    def add_input(self, new_input):
        if self._current_group is None:
            self._current_group = []
            self._groups.append(self._current_group)
        self._current_group.append(new_input)

    def finalise_group(self):
        self._current_group = None

    @property
    def groups(self):
        return self._groups

    @property
    def current_group(self):
        return self._current_group

    def __str__(self):
        temp = ""
        for group in self._groups:
            for text in group:
                temp += text + "\n"
            temp += "\n"
        return temp
