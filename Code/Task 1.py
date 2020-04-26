# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:20:34 2020

@author: DM
"""

def CG_content_calculator(seq):    
    counterCG = 0
    for i in range(0,len(seq)):
        if seq[i] == 'C' or seq[i] == 'G':
            counterCG = counterCG + 1    
    CG_content = counterCG/len(seq)
    print ('%.2f%%' % (CG_content*100))
seq='ATCAGATC'
CG_content_calculator(seq)
