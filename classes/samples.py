from base.item import Item

class Samples(Item):
    collection_name = 'samples'
    collection_schema = {
        'sample': 1,
        'methylationContext':1,
        'srx': 1,
        'protocol': 1
    }

    def __init__(self):
        super(Samples, self).__init__()
