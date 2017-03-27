#catfasta2phyml riscritto in pyhton

import sys
import fileinput
from Bio import SeqIO

outputhandle = open("concatenato.fasta", "w")


try:
    sys.argv[1]
except Exception as e:
    print("NO INPUT")
    exit()
outputdict = {}
for line in sys.argv[1:]:

    for record in SeqIO.parse(line, "fasta"):
        idi = str(record.id)
        seq = record.seq
        if idi not in outputdict.keys():
            outputdict[idi] = ""
            outputdict[idi] += seq
        else:
            outputdict[idi] += seq


for key in outputdict.keys():
    outputhandle.write(">%s\n%s\n" %(key, outputdict[key]))

outputhandle.close()
