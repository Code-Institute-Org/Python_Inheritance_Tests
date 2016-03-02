from seabird import Seabird


class Penguin(Seabird):
    @property
    def description(self):
        return super(Penguin, self).description
