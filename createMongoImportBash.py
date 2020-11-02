import sys
import json
import os.path

fileSamples = open(sys.argv[1],'r')
fileBatch = open(sys.argv[2],'r')

chromsAllowed = {"chr1":"","chr2":"","chr3":"","chr4":"","chr5":"","chr6":"","chr7":"","chr8":"","chr9":"","chr10":"","chr11":"","chr12":"","chr13":"","chr14":"","chr15":"","chr16":"","chr17":"","chr18":"","chr19":"","chr20":"","chr21":"","chr22":"","chrM":"","chrX":"","chrY":"","chrEBV":""}
for line in fileSamples:
    for chrom in chromsAllowed:
        fname = line.strip()+"_"+chrom+".json"
        if os.path.isfile(fname):
            escribir = "mongoimport --host localhost:8028 --db hg38 --collection "+chrom+" --file="+fname+" --jsonArray --mode=merge\n"
            fileBatch.write(escribir)

fileBatch.close()
