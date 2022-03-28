# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:29:05 2022

@author: adminstrator
"""

file = input("Enter a name of the file: ")

name = open(file, "r")
word=name.read()
name.close()

s = "".join([char.lower() for char in word if char.isalpha()])

word_dict = {}
unique_char = ""
for char in s:
    if char not in unique_char:
        unique_char += char      
    
for char in sorted(unique_char):
    key = char
    value = s.count(char)
    word_dict[key] = value

new_dict = dict(sorted(word_dict.items(), key = lambda item: item[1], reverse=True))  
for k, v in new_dict.items():
    print(k, "-->", v)
    
try:
    fo = open(file, "a")
    sum = "\n\nSummary for characters: \n\n"
    for ch in sum:
        fo.write(ch)
    for k, v in new_dict.items():
        line = k, "-->", str(v),"\n"  
        for char in line:
            fo.write(char)
    fo.close()
except Exception as e:
    print(e)