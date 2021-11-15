DNA = ['A', 'T', 'C', 'G']

file = open('rosalind_dna.txt', 'r')

DNA = file.read().strip()

def sequenceValidate(dna_seq):
    the_DNA  = dna_seq.upper()
    for nuc in the_DNA:
        if nuc not in the_DNA:
            return False
        else: pass

    return the_DNA

def nucleotide_counter(nucleotide):
    DNA = sequenceValidate(nucleotide)
    nucleotides = {}
    try:
        for nuc in DNA:
            nucleotides[nuc] = nucleotides.get(nuc, 0) +1

        return nucleotides
    except:
        raise('Not a valid nucleotide')

print(nucleotide_counter(DNA))


