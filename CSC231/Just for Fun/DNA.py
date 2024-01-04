def checkStrand(line):
    for index in line:
        if index not in ('A,T,C,G'):
            return False
    return True

Dna_strand = input('Please enter a DNA Strand: ')
Base_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
check=checkStrand(Dna_strand)
compl_strand = ''
while check==False:
    Dna_strand = input('Please enter a DNA Strand with no characters other than A,G,C,T: ')
    check = checkStrand(Dna_strand)
for index in Dna_strand:
    compl_strand = compl_strand + Base_dict[index]
print(compl_strand)
