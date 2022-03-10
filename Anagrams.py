# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 16:04:02 2022

@author: adminstrator
"""


#anagrams:asks the user for two separate texts;
#checks whether, the entered texts are anagrams and prints the result.

text1 = input("Enter a text: ")
text2 = input("Enter another text: ")


list1 = [char for char in text1.lower()]
list2 = [char for char in text2.lower()]

if sorted(list1) == sorted(list2):
    print("They are anagrams.")
else:  
    print("They are not anagrams")

#solution 2 with removing spaces 

text1 = input("Enter a text: ")
text2 = input("Enter another text: ")

list1=[]
list2=[]

for char in text1:
    if char.isalnum():
        list1.append(char.lower())
        
for char in text2:
    if char.isalnum():
        list2.append(char.lower())
        
string1=""
string2=""
    
for e in sorted(list1):
    string1 += e
    
for e in sorted(list2):
    string2 += e
    
if string1 == string2:
    print("They are anagrams.")
else:  
    print("They are not anagrams")