class ScriptParser(object):
    def __init__(self, iset, ilist_factory):
        self._iset = iset
        self._ilist_factory = ilist_factory

    def parse(self, script):
        if type(script) is str:
            _script = script.splitlines()
        else:
            _script = script
        return self._parse(_script)

    def _parse(self, script):
        cur_ilist = self._ilist_factory()
        istack = stack()
        for line in script:
            instruction = self._iset.match_string(line)
            if instruction is None:
                continue

            if instruction.BEFORE == "branch":
                branch = cur_ilist
                (parent, cur_ilist) = istack.pop()
                cur_ilist.add(parent, branch)
            if instruction.AFTER == "branch":
                istack.push((instruction, cur_ilist))
                cur_ilist = self._ilist_factory()
            else:
                cur_ilist.add(instruction)
        return cur_ilist

class stack(list):
    def push(self, item):
        self.append(item)
