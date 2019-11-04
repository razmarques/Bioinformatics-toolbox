"""
This module groups functions that simulate bioinformatics data
"""

import random


def generate_random_sequence(sequence_size, type):
    """
    Generates a random nucleotide sequence of a given type (DNA or RNA)
    Arguments:
         sequence_size (int) -- number of base pairs of the nucleotide sequence
         type (string) -- defines the type of the nucleotide sequence: "dna" or "rna"

     Returns:
         sequence (string) -- sequence of nucleotides
    """

    sequence = ""
    if type == "dna":
        nucleotides = ("A", "T", "C", "G")
    elif type == "rna":
        nucleotides = ("A", "U", "C", "G")

    for inuc in range(sequence_size):
        sequence += random.choice(nucleotides)

    return sequence
