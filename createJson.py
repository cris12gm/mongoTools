import sys
import json

fileMeth = open(sys.argv[1],'r')
individual = sys.argv[2]
sample = sys.argv[3]
out = sys.argv[1]+".json"

values = []
n = 0
for line in fileMeth:
    n = n + 1
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
    sampleValues = {sample:{"methRatio":methylation,"pScore":quality,"coverage":coverage}}
    value = {"_id":_id, "chrom":chrom, "pos":chromStart,'methylation_CG.'+individual:sampleValues}
    values.append(value)
print ("End")

with open(out, 'w') as outfile:
    json.dump(values, outfile)