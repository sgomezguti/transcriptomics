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

key_name = ''

for line in raw:
    if not line.find('>'):
        seqs_dic[line] = []
        key_name = line
    else:
        seqs_dic[key_name].append(line)

#for k, v in seqs_dic.items():
#    print(k,v)

new_dict = {}
modified_keys = []

incremental_number = 1
#Iterate over the original dictionary
for key, value in seqs_dic.items():
    # Modify the key
    #modified_key = 'Pmaydis' + key.rsplit('/',1)[1]
    #modified_key = 'P_maydis' + key.split("/",1)
    modified_key_one = key.replace("m64269e", "Pmaydis")
    modified_key_two = modified_key_one.split("_",1)
    # Get the prefix before the first "_"
    prefix = modified_key_two[0]
    # Construct the output string with the incremental number
    modified_key = prefix + "_" + str(incremental_number)
    incremental_number += 1
    modified_keys.append(modified_key)
    # Add the modified key and the corresponding value to the new dictionary
    new_dict[modified_key] = value

#print("The original list id :" + str(modified_keys))

flag = 0
# using set() + len()
# to check all unique list elements
flag = len(set(modified_keys)) == len(modified_keys)

#printing result
if(flag):
    print("List contains all unique elements")
else:
    print(("List contains does not contains all unique elements"))

# Print the new dictionary
#print(len(new_dict))
#for k, v in new_dict.items():
#    print(k, v)

pacbio_last = []
print(modified_keys)
for id in modified_keys:
    if id in new_dict.keys():
        pacbio_last.append(id + '\n')
        ## Extract each line from the sequence list
        for seq in new_dict[id]:
            pacbio_last.append(seq + '\n')

with open('/scratch/negishi/sgomezgu/phylachora_maydis/pacbio_raw/pacbio_from_beggining/fasta_ok/raw_pacbio_ok.fa', 'w') as pacbio_fasta:
    pacbio_fasta.writelines(pacbio_last)

