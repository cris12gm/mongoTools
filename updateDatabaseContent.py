import sys
import json
from classes.databaseContent import Content
from base.mongo_engine import MongoEngine

fileContent = open(sys.argv[1],'r')

MongoEngine().set_database_name('hg38')

d = {}
for line in fileContent:
    line = line.strip().split("\t")
    d = {
        '_id':line[0],
        'specie': line[1],
        'assembly': line[2],
        'individual': line[3],
        'sample': line[4],
        'context': line[5],
        'sex': line[6],
        'age': line[7],
        'physiopatological_status': line[8],
        'description': line[9],
        'reference': line[10],
        'biosample': line[11],
        'srx':line[12],
        'dump5': line[13]
    }
    Content().insert(d)

