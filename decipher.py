# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 16:04:02 2022

@author: adminstrator
"""


#Caesar cipher improved

message = input("Enter a message: ")
shift_value = int(input("Enter a number between 1 to 25: "))

if shift_value < 1:
    print("shift_value too low.")
elif shift_value > 25:
    print("shift_value too high.")

cipher = ""   
for char in message:
    if not char.isalpha():
        code = chr(ord(char))
    elif char.islower():
        if ord(char)+shift_value>=123:
            code = chr(97+(ord(char)+shift_value-123))
        else:    
            code = chr(ord(char)+shift_value)
    elif char.isupper():
        if ord(char)+shift_value>=91:
            code = chr(65+(ord(char)+shift_value-91))
        else:
            code = chr(ord(char)+shift_value)
            
    cipher+=code
    
print(cipher)

    