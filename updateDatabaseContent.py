import sys
import json
from classes.databaseContent import Content
from base.mongo_engine import MongoEngine

fileContent = open(sys.argv[1],'r')

MongoEngine().set_database_name('hg38')

d = {}
for line in fileContent:
    line = line.strip().split("\t")
    Content().insert({
        '_id': str(line[0]),
        'specie': str(line[1]),
        'assembly': str(line[2]),
        'individual': str(line[3]),
        'sample': str(line[4]),
        'project': str(line[5]),
        'context': str(line[6]),
        'sex': str(line[7]),
        'age': str(line[8]),
        'physiopatological_status': str(line[9]),
        'description': str(line[10]),
        'reference': str(line[11]),
        'biosample': str(line[12]),
        'srx':str(line[13]),
        'dump5': str(line[14])
    })

