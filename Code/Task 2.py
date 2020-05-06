# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 09:42:11 2020

@author: 17426
"""
import re
#define the function
def complementary_strand(seq):
    #check if the input sequence is a correct DNA sequence, if not exit the function and give an error message
    if re.search(r'[^ATCGactg]',seq):
        return("not a correct DNA sequence") 
    #change lower case to upper case
    seq=seq.upper()
    #replace A/T/C/G with t/a/g/c, use lower case to avoid confusing variable assignments 
    seq=seq.replace('A','t').replace('C','g').replace('G','c').replace('T','a')
    #change lower case to upper case
    seq=seq.upper()
    #change 3'->5' sequence to 5'->3' sequence
    seq=seq[::-1]
    #output sequence
    return(seq)

s='ATTAAACCCTCGTGAC'
print('The complementary strand: '+complementary_strand(s))
        