import sys
import json

fileMeth = open(sys.argv[1],'r')
individual = sys.argv[2]
sample = sys.argv[3]
context = sys.argv[4]

valuesByChrom = {}
n = 0
for line in fileMeth:
    n = n + 1
    if "chrom" in line:
        continue
    line = line.strip().split("\t")
    chrom = line[0]
    chromStart = line[1]
    _id = chrom+"_"+chromStart
    coverage = int(line[4])
    methylation = float(float(line[5])/float(line[4]))
    sampleValues = {sample:{"methRatio":methylation,"coverage":coverage}}
    if context=="CG":
        value = {"_id":_id, "chrom":chrom, "pos":chromStart,'methylation_CG.'+individual:sampleValues}
    elif context=="CHG":
        value = {"_id":_id, "chrom":chrom, "pos":chromStart,'methylation_CHG.'+individual:sampleValues}
    try:
        ch = valuesByChrom[chrom] 
    except:
        ch = []
    ch.append(value)
    valuesByChrom[chrom] = ch

print ("End")

chromsAllowed = {"chr1":"","chr2":"","chr3":"","chr4":"","chr5":"","chr6":"","chr7":"","chr8":"","chr9":"","chr10":"","chr11":"","chr12":"","chr13":"","chr14":"","chr15":"","chr16":"","chr17":"","chr18":"","chr19":"","chr20":"","chr21":"","chr22":"","chrM":"","chrX":"","chrY":"","chrEBV":""}
for chrom in valuesByChrom:
    if chrom in chromsAllowed:
        out = sys.argv[1]+"_"+chrom+".json"    
        with open(out, 'w') as outfile:
            json.dump(valuesByChrom[chrom], outfile)