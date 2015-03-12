from .base import FormatterBase

class NewlineFormatter(FormatterBase):
    '''
    Each item in a group is separated by a newline.
    Each group is also separated by newline.
    '''
    def format(self, collector):
        temp = ""
        for group in collector.groups:
            for text in group:
                temp += text + "\n"
            temp += "\n"
        return temp
