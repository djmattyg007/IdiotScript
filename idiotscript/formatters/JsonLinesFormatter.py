from .base import FormatterBase
import json

class JsonLinesFormatter(FormatterBase):
    '''
    Each item in a group is an individual item in a single
    line of a JSON array. Each group is its own JSON line.
    '''
    def format(self, collector, ensure_ascii = False):
        '''
        json.dump() expect to deal only with IO objects, so
        we need to use StringIO, which wraps a string in an
        IO object, and then capture the output.
        '''
        from io import StringIO
        io_obj = StringIO()
        self._format(collector, io_obj, ensure_ascii)
        value = io_obj.getvalue()
        io_obj.close()
        return value

    def write_file(self, collector, filename, ensure_ascii = False):
        with open(filename, 'w') as out_file:
            self._format(collector, out_file, ensure_ascii)

    def _format(self, collector, io_obj, ensure_ascii = False):
        for group in collector.groups:
            json.dump(group, io_obj, ensure_ascii = ensure_ascii)
            io_obj.write("\n")
