#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:25:30 2019

@author: vyom
"""
def Intelligence_level():
    
    for y in range (1,7):
        x = 5.5
        l=[y]
        m=[]
        n=[]
        while x <= 12.5:
            i = 2 * ( y + 0.5 * x )
            m.append(x)
            n.append(i)
            x = x + 0.5
        print( m)
        print(*l ,sep='\n')
Intelligence_level()
    
    
    
    
    
    
    