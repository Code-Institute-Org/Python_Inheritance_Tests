import abc

class Bird(object):
    def __init__(self, kind, call):
        self.kind = kind
        self.call = call
    @property
    def description(self):
        return 'A %s goes %s' % (self.kind, self.call)
