import sys
import json
from classes.methylation import Methylation
from classes.samples import Samples
from base.mongo_engine import MongoEngine

fileMeth = open(sys.argv[1],'r')
sampleName = sys.argv[2]
srx = sys.argv[3]
protocol = sys.argv[4]

context = "CG"

MongoEngine().set_database_name('hg38')
Samples().insert({'sample':sampleName, 'methylationContext' : "CG", 'srx':srx, 'protocol':protocol})

for line in fileMeth:
    if "#" in line:
            continue
    line = line.replace(".","0")
    line = line.strip().split("\t")
    chrom = line[0]
    chromStart = line[1]
    _id = chrom+"_"+chromStart
    methylated = int(line[3])+int(line[6])
    coverage = int(line[4])+int(line[7])
    qualityW = float(line[5])*float(line[4])
    qualityC = float(line[8])*float(line[7])
    quality = (qualityW + qualityC) / float(coverage)
    methylation = str(round((methylated/quality),2))
    values = {'methylation_CG.'+sampleName:{"methRatio":methylation,"pScore":quality}}
    values_Insert = {sampleName: {"methRatio":methylation,"pScore":quality}}
    # 1 Check if possition is stored
    checkPos = Methylation().find({'_id': _id})

    if checkPos.data:
        #2. Update if position exists
        Methylation().update({"_id": _id}, values)
    else:
        #3. If it is first time, insert
        Methylation().insert({'_id': _id, 'methylation_CG' : values_Insert})

