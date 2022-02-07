#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:27:06 2022

@author: sjcet
"""
#Qs2. Write a program to bubblesort on a given set of elements?
def bubble_sort(list1):
    # Outer loop for traverse the entire list
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if (list1[j] > list1[j + 1]):
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp
    return list1


list1 = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", list1)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(list1))