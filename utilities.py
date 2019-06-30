"""
This module contains several functions for basic computations with nucleotides
"""


def count_nucleotides(seq):
    nuc_counter = {'A':0, 'C':0, 'G':0, 'T':0, 'U':0}
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


def thymine_to_uracil(dnaseq):
    rnaseq = dnaseq.replace("T", "U")
    return rnaseq
