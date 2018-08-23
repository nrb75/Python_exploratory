#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 13:49:24 2018

@author: natalie
"""

dice=[1,2,3,4,5,6]
count=[0]*10
count2=0
import random

for x in range(10):
    count2=0
    while random.choice(dice)<6:
        count2 += 1
    count[x]=count2
print(count)


count1=0
while random.choice(dice)<6:
    count1+=1
print(count1)