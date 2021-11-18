#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:00:34 2021

@author: anil
"""

'''
1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
in a comma-separated sequence on a single line.
'''

j = []
#print(a)
for u in range(2000,3200+1):
    #print(u)
    if u%7 == 0 and u%5!= 0:
        print(u)
        j.append(u)
        
        
        
        

'''
2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
'''

first_name = input("enter your first name:")
last_name = input("enter your last name:")
ful_name = first_name+ " "+last_name
#print(ful_name)
print(ful_name[::-1])



'''
3. Write a Python program to find the volume of a sphere with diameter 12 cm. Formula: V=4/3 * π * r 3
'''

'''
method1
'''

diameter = int(input("enter diameter:"))
r = diameter/2
pi = 22/7
v = 4/3 * pi *r**3
print(v)

'''
method2
'''

def formula():
    d = int(input("enter diameter:"))
    r = d/2
    pi = 22/7
    v = 4/3 * pi * r**3
    print("volume of sphere:", v)
    
    
formula()    
    
    
    
    
