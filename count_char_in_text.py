# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 22:18:21 2022

@author: adminstrator
"""

file = input("Enter a name of the file: ")

import os

name = open(file, "rt")
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
    
for k, v in word_dict.items():
    print(k, ">", v)