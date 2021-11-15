def sequenceValidate(nuc_seq, nuc_type):
    """Checks if a sequence is a valid nucleotide sequence."""

    DNA = ['A', 'T', 'C', 'G']
    RNA = ['A', 'U', 'C', 'G']
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
    DNA_complements = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    "Returns a reverse complement of a single strand"
    return ''.join([DNA_complements[nuc] for nuc in DNA])[::-1]
