from .base import FormatterBase

class NewlineFormatter(FormatterBase):
    def format(self, collector):
        temp = ""
        for group in collector.groups:
            for text in group:
                temp += text + "\n"
            temp += "\n"
        return temp
