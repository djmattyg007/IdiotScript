class Collector(object):
    def __init__(self):
        self._groups = []
        self._current_group = None

    def add_input(self, new_input):
        '''
        The current group is the group that inputs are added to.
        We need to check to see if one exists before we can save
        input we've been given.
        '''
        if self._current_group is None:
            # If one doesn't exist, create it, and add it to the
            # main list of groups.
            self._current_group = []
            self._groups.append(self._current_group)
        self._current_group.append(new_input)

    def new_group(self):
        '''
        This method doesn't actually create a new group. Groups
        are created lazily when needed inside the add_input method.
        By setting the current group to None, we ensure that a
        new group will be created as soon as it is necessary.
        '''
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
