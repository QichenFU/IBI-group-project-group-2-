# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:08:31 2020

@author: 92801
"""
DNA = 'ATCGCCGTAC' #The of coding DNA strand that you want to convert to RNA sequence

def transcribe(i):
    RNA_sequence = i.replace('T', 'U')
    return(RNA_sequence)

print('RNA= ',transcribe(DNA))