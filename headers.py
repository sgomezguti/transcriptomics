"""=================================================================================================
Headers
Change the headers in a Pacbio fasta file so each identifier is unique for each individual
read.
================================================================================================="""
pacbio="/scratch/negishi/sgomezgu/phylachora_maydis/pacbio_raw/pacbio_from_beggining/fasta_ok/raw_reads.fa"
headers={}

infile=open(pacbio, 'r')

raw = infile.readlines()

#for i in infile:
#    if i.startswith(">"):
#        print(i)

## Remove newline characters from all elements on the lists
for i in range(0, len(raw)):
    raw[i] = raw[i].rstrip('\n')

seqs_dic = {}
count = 0

for line in raw:
    if not line.find('>'):
        seqs_dic[line] = []
        key_name = line
    else:
        seqs_dic[key_name].append(line)


print(seqs_dic)