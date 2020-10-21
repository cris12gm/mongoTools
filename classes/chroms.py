from base.item import Item

class Chroms(Item):
    collection_name= 'chromSizes'
    collection_schema = {
        'chrom' : 1,
        'size' : 1
    }

    def __init__(self):
        super(Chroms, self).__init__()
