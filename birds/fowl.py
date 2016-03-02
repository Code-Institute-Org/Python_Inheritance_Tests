from birds.bird import Bird


class Fowl(Bird):
    def __init__(self, kind, call, type):
        self.fowl_types = {'landfowl': 'Landfowl is an order of heavy-bodied ground-feeding birds that includes\n'
                                       'turkey, grouse, chicken, New World quail and Old World quail,\n'
                                       'ptarmigan, partridge, pheasant, junglefowl and the Cracidae\n',
                           'waterfowl': 'Waterfowl is an order of birds that comprises about 180 living species\n'
                                        'in three families: Anhimidae (the screamers), Anseranatidae\n'
                                        '(the magpie goose), and Anatidae,the largest family, which\n'
                                        'includes over 170 species of waterfowl,\n'
                                        'among them the ducks, geese, and swans.\n'}
        self.type = type
        super(Fowl, self).__init__(kind, call)

    @property
    def description(self):
        return super(Fowl, self).description + '\n' + 'Some interesting facts about the %s : A %s is of type %s. %s' \
                                                      % (self.kind, self.kind, self.type,
                                                         self.fowl_types[self.type.lower()])
