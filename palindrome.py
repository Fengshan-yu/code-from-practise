# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 04:19:37 2022

@author: adminstrator
"""

#check whether a phrase is palindrome



import math


phrase = input("Enter a phrase: ")

new_phrase = "".join([char.lower() for char in phrase if char.isalpha()])

if len(new_phrase) <= 1:
    print("Yes")
    
elif len(new_phrase)%2==0:
    a=int(len(new_phrase)/2)
    strng1=new_phrase[0: a]
    strng2=new_phrase[a:]
    strng3=strng2[::-1]
    if strng1==strng3:
        print("Yes")
    else:
        print("No")    
else:
    x=math.floor(len(new_phrase)/2)
    strng1=new_phrase[0: x+1]
    strng2=new_phrase[x:]
    strng3=strng2[::-1]
    
    if strng1==strng3:
        print("Yes")
    else:
        print("No")
        
        
# recursive palindrome

def ispal(text):
    
    s = "".join([char.lower() for char in text if char.isalpha()])
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and ispal(s[1: -1])
    
