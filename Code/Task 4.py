# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:41:56 2020

@author: 蒋冰
"""
import re
#define the function
def mRNA_protein(RNA_string):
    #check if the input sequence is a correct RNA sequence, if not exit the function and give an error message
    if re.search(r'[^AUCGacug]',RNA_string):
        return("not a correct RNA sequence") 
    #change lower case to upper case
    RNA_string=RNA_string.upper()
    #input the genetic code dictionary
    start_code = 'AUG'
    protein_table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 
                     'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V', 
                     'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V', 
                     'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
                     'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', 
                     'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 
                     'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 
                     'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 
                     'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D', 
                     'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 
                     'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 
                     'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 
                     'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 
                     'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G', 
                     'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
                     'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}
    #find start codon
    start_sit = re.search(start_code, RNA_string)
    protein = ''
    #if sart codon exist, translate until we meet the stop codon
    if RNA_string.find('AUG') > -1:
        for sit in range(start_sit.end() - 3, len(RNA_string), 3):
            if protein_table[RNA_string[sit:sit+3]] == 'Stop':
                break
            else:
                protein = protein + protein_table[RNA_string[sit:sit+3]]
        return('The peptide translated from mRNA is: '+protein)
    # cannot find start codon
    else:
        return('cannot find start codon')
    #output the result

RNA_string ='CGCGCGCGAUGCUUAUUGUGGCCGCGGAUAACUAAGGC'
print(mRNA_protein(RNA_string))
    










