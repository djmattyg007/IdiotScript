from .base import FormatterBase
import csv

class CsvFormatter(FormatterBase):
    '''
    Each item in a group is an individual cell in a single
    CSV row. Each group is its own CSV row.
    '''
    def format(self, collector):
        '''
        csv.writer expects to deal only with IO objects, so
        we need to use StringIO, which wraps a string in an
        IO object, and then capture the output.
        '''
        from io import StringIO
        io_obj = StringIO()
        self._format(collector, io_obj)
        value = io_obj.getvalue()
        io_obj.close()
        return value

    def write_file(self, collector, filename):
        with open(filename, 'w') as out_file:
            self._format(collector, out_file)

    def _format(self, collector, io_obj):
        writer = csv.writer(io_obj, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for group in collector.groups:
            writer.writerow(group)
