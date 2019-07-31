# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:12:38 2019

@author: SCL1
"""

sumA = 0
nA = int(input("Enter number of terms: "))
x = int(input("Enter x: "))
for i in range(1,nA+1):
    sumA += (x**i)/i
print(sumA)

sumB = 0
nB = int(input("Enter number of terms: "))
for j in range(1,nB+1):
    sumB += j/((j+1)**(1/2))
print(sumB)