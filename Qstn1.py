#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 15:27:16 2022

@author: sjcet
"""
import numpy as np

array = np.arange(20)    # dummy array

result = []    # a seperate list for storing odd numbers

for i in array:

 if i % 2 != 0:

   result.append(i)

print(np.array(result))
a = np.arange(1, 11, 1)
print(a)
first_element = a[:4]
print(first_element)
first_element1 = a[5:]
print(first_element1)
first_element2 = a[1:7]
print(first_element2)