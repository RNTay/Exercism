#!/usr/bin/env python3

def proteins(strand):
    codons = [''.join(list(strand[_:_+3])) for _ in range(0, len(strand), 3)]

    codon_to_protein = {'AUG': 'Methionine',
                        'UUU': 'Phenylalanine',
                        'UUC': 'Phenylalanine',
                        'UUA': 'Leucine',
                        'UUG': 'Leucine',
                        'UCU': 'Serine',
                        'UCC': 'Serine',
                        'UCA': 'Serine',
                        'UCG': 'Serine',
                        'UAU': 'Tyrosine',
                        'UAC': 'Tyrosine',
                        'UGU': 'Cysteine',
                        'UGC': 'Cysteine',
                        'UGG': 'Tryptophan',
                        'UAA': 'STOP',
                        'UAG': 'STOP',
                        'UGA': 'STOP'}

    protein_translations = [codon_to_protein[codons[_]] for _ in range(len(codons))]
    for protein_index in range(len(protein_translations)):
        protein = protein_translations[protein_index]
        if protein == 'STOP':
            protein_translations = protein_translations[:protein_index]
            break
    return protein_translations
