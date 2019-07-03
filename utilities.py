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


def compute_reverse_complement(dnaseq):
    dna_comp = compute_dna_complement(dnaseq)
    return dna_comp[::-1] # returns the reverse of dna_comp string


def thymine_to_uracil(dnaseq):
    rnaseq = dnaseq.replace("T", "U")
    return rnaseq
