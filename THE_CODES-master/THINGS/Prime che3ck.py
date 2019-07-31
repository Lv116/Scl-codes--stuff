# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 08:33:25 2019

@author: SCL1
"""
def prime_num():
    
    x=int(input('Enter the number that you want to check-'))
    y=2
    z=0
    l=1
    while(z!=1):
        if(x!=2):
            z=x/y
            y=y+1
            if (z==1):
                l=0
                break

    if (l!=0):
        print(f'{x} is prime')
    else:
        print(f'{x} is not prime.')    
        
prime_num()