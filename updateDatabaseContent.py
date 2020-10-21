import sys
import json
from classes.databaseContent import Content
from base.mongo_engine import MongoEngine

fileContent = open(sys.argv[1],'r')

MongoEngine().set_database_name('hg38')

for line in fileContent:
    print (line)
#Content().insert({'sample':sampleName, 'methylationContext' : "CG"})

