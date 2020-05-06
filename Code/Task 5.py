# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:00:50 2020

@author: 梦之起点


"""

import re

def find_cutting_sites(DNA_style,DNA_sequence,recognition_sequence):
   location='The locations of cutting sites:' #record the locations 
   count=0 #record the number of cutting sites
   a=False #record whether the cutting sites are found or not
   #check whether the input DNA_style is correct
   if DNA_style != 'ring' and DNA_style != 'linear':
       return("Please input correct DNA style")
   #check whether the input sequence is a correct DNA sequence
   if re.search(r'[^ATCGactg]',DNA_sequence):
       return("not a correct DNA string") 
   #check whether the input sequence is a correct recognition_sequence
   if re.search(r'[^ATCGactg]',recognition_sequence):
       return("not a correct recognition sequence") 
   #change lowercase to uppercase if the input contains lowercase(atcg)
   DNA_sequence=DNA_sequence.upper()
   recognition_sequence=recognition_sequence.upper()
   #prolong the DNA ring to find cutting sites
   if DNA_style=='ring':
       DNA_sequence += DNA_sequence[0:len(recognition_sequence)-1]    
   #find cutting sites
   for i in range(len(DNA_sequence)):
       if  DNA_sequence[i:i+len(recognition_sequence)] == recognition_sequence:
          count+=1   #record the number of the cutting sites
          location =location + str(i+1) + ',' #record the locations
          a=True  #record that the cutting site(s) is/are found
   location=location[:-1]    
   if a : print(location) #if cutting site(s) is/are found, output the location(s)
   return("The number of cutting sites:"+str(count))

#input DNA style, string and the recognition sequence of restriction enzyme
DNA_style= input('Please choose the DNA style (ring or linear):')
DNA_sequence= input ('Please input the DNA sequence:')
recognition_sequence= input ('Please input the recognition sequence:')
       
#output the results
print(find_cutting_sites(DNA_style,DNA_sequence,recognition_sequence))    

    
      
        
        
    
    



