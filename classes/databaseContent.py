from base.item import Item

class Content(Item):
    collection_name = 'databaseContent'
    collection_schema = {
        'specie': 1,
        'assembly': 1,
        'individual': 1,
        'sample': 1,
        'context': 1,
        'sex': 1,
        'age': 1,
        'physiopatological_status': 1,
        'description': 1,
        'reference': 1,
        'biosample': 1,
        'srx':1,
        'dump5': 1
    }

    def __init__(self):
        super(Content, self).__init__()
