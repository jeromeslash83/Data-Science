from Genetic_structures import *


def sequenceValidate(nuc_seq, nuc_type):
    """Checks if a sequence is a valid nucleotide sequence."""

    if nuc_type == 'DNA':
        the_DNA  = nuc_seq.upper()
        for nuc in the_DNA:
            if nuc not in DNA:
                return False
            else: pass

        return the_DNA
    else:
        the_RNA  = nuc_seq.upper()
        for nuc in the_RNA:
            if nuc not in RNA:
                return False
            else: pass

        return the_RNA


def nucleotide_counter(nucleotide):
    """Gives the proportion of the number of nucleotides in a given sequence."""

    nucs = nucleotide
    nucleotides = {}
    try:
        for nuc in nucs:
            nucleotides[nuc] = nucleotides.get(nuc, 0) +1

        return nucleotides
    except:
        raise('Not a valid nucleotide')
        

def RNA_transcription(DNA):
    """Transcribes DNA into RNA sequence."""
    return DNA.replace('T', 'U')


def reverse_complementation(DNA):
    "Returns a reverse complement of a single strand"
    return ''.join([DNA_complements[nuc] for nuc in DNA])[::-1]


def GC_content(sequence):
    """Returns the percentage of G's and C's of a certain nucleotide sequence."""

    return ((sequence.count('C') + sequence.count('G'))/ len(sequence)) * 100



def GC_content_sub(sequence, k = 1):
    """Returns the percentage of G's and C's of a certain nucleotide subsection of a nucleotide sequence."""

    subsection = []
    for n in range(len(sequence) + 1 - k, k):
        subsequence = sequence[n:(n + k)]
        subsection.append(GC_content(subsequence))
    return subsection



def translate_nuc(seq, type, initial = 0):
    """Translates an RNA(codons) into amino acid sequence. 
    Use type (list or string) to return which type do you like your sequence to be."""
    if type == 'list':
        return [RNA_Codons[seq[pos:pos+3]] for pos in range(initial, (len(seq) - 2), 3)]
    else:
        aa_seq = ''
        for pos in range(initial, (len(seq) - 2), 3):
            if RNA_Codons[seq[pos:pos+3]] == '_':
                aa_seq += '_'
                break
            else:
                aa_seq += (RNA_Codons[seq[pos:pos+3]] + '-')
        return aa_seq
                

