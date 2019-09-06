"""
This module groups functions that simulate bioinformatics data
"""

import random


def generate_random_sequence(sequence_size, type):

    sequence = ""
    if type == "dna":
        nucleotides = ("A", "T", "C", "G")
    elif type == "rna":
        nucleotides = ("A", "U", "C", "G")

    for inuc in range(sequence_size):
        sequence += random.choice(nucleotides)

    return sequence
