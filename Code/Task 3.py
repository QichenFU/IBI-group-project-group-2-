# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:08:31 2020

@author: 92801
"""
import re
import sys
#define the function
def transcription(seq):
    #check if the input sequence is a correct DNA sequence, if not exit the function and give an error message
    if re.search(r'[^ATCGactg]',seq):
        print("not a correct DNA sequence") 
        sys.exit()
    #change lowercase to uppercase if the input contains lowercase
    seq=seq.upper()
    #converting coding strand to mRNA only requires changing T to U
    seq=seq.replace('T', 'U')
    return(seq)

DNA = 'ATCGCCTAC' #The coding DNA strand that you want to transcript
print('RNA=',transcription(DNA))