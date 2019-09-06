"""
This module contains several functions for basic computations with nucleotides
"""


def compute_dna_complement(dna_seq):
    seq_c = ''
    for nuc in dna_seq:
        if nuc == 'A':
            seq_c += 'T'
        elif nuc == 'T':
            seq_c += 'A'
        elif nuc == 'C':
            seq_c += 'G'
        elif nuc == 'G':
            seq_c += 'C'
        else:
            raise ValueError("Unrecognized nucleotide")
    return seq_c


def compute_gc_content(dna_seq):
    dna_size = len(dna_seq)
    nuc_count = count_nucleotides(dna_seq)

    return (nuc_count['G'] + nuc_count['C'])/dna_size


def compute_reverse_complement(dna_seq):
    dna_comp = compute_dna_complement(dna_seq)
    return dna_comp[::-1] # returns the reverse of dna_comp string


def count_nucleotides(seq):
    nuc_counter = {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'U': 0}
    for nuc in seq:
        if nuc == 'A':
            nuc_counter['A'] += 1
        elif nuc == 'C':
            nuc_counter['C'] += 1
        elif nuc == 'G':
            nuc_counter['G'] += 1
        elif nuc == 'T':
            nuc_counter['T'] += 1
        elif nuc == 'U':
            nuc_counter['U'] += 1
        else:
            raise ValueError("Unrecognized nucleotide")
    return nuc_counter


def count_point_mutations(seq_1, seq_2):
    """
    This function computes the number of point mutations of two sequences of equal length.
    This is equivalent to the Hammond distance between two strings
    """
    if not len(seq_1) == len(seq_2):
        raise ValueError("The sequences in both arguments should be of equal length")

    counter = 0
    for inuc in range(len(seq_1)):
        if not seq_1[inuc] == seq_2[inuc]:
            counter += 1
    return counter


def thymine_to_uracil(dna_seq):
    rna_seq = dna_seq.replace("T", "U")
    return rna_seq
