# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:20:34 2020

@author: DM
"""
import re
#define the function
def CG_content_calculator(seq):
    #check if the input sequence is a correct DNA sequence, if not exit the function and give an error message
    if re.search(r'[^ATCGactg]',seq):
        return("not a correct DNA sequence") 
    #change lower case to upper case
    seq=seq.upper()
    #set the initial GC content to 0
    counterCG = 0
    #use for loop to count the number of CG 
    for i in range(0,len(seq)):
        if seq[i] == 'C' or seq[i] == 'G':
            counterCG = counterCG + 1    
    CG_content = counterCG/len(seq)
    #calculate and output the CG content
    return ('%.2f%%' % (CG_content*100))

seq='ATCAAGTGACCTA'
print(CG_content_calculator(seq))