from birds.bird import Bird


class Seabird(Bird):
    def __init__(self, kind, call, diving_depth):
        self.diving_depth = diving_depth
        super(Seabird, self).__init__(kind, call)

    @property
    def description(self):
        return super(Seabird, self).description + '\n' + 'and also, a %s dives to a depth of %s metres' % (
        self.kind, self.diving_depth)
