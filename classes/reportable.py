class Reportable:

    def __init__(self, object):
        self.object = object

    def to_report_line(self):
        self.object = str(self.object)
        if not self.object:
            raise Exception ("NotImplementedError")