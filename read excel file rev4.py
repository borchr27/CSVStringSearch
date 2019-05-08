#!/usr/bin/env python3
#read excel file rev4

import os
import csv
import re

global newArray
newArray = []
finalArray = []
count = 0


def Search(key = str(input())):
    global count, finalArray
    key = key.lower()
    key = key.split(' ')
    
    FirstWordSearch(key)
    #print(newArray, len(newArray))
    
    while count < len(key):
        FollowingWordsSearch(key,newArray,count)
        count += 1
        
    finalArray = list(dict.fromkeys(finalArray))
    print(finalArray)


def FirstWordSearch(a):
    with open('CMC cycle time data.csv') as csvfile:
        csv_file = csv.reader(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_NONE) 
        
                 
        for row in csv_file:

            description = row[0]
            #ct = row[1] #cycle time
            #units = row[2]
        
            if description.find(a[0]) != -1:
                newArray.append(description)
            else: pass
        print(newArray)    

def FollowingWordsSearch(key,newArray,count):
    i = 0
    while i < len(newArray):
        if newArray[i].find(key[count]) != -1:
            finalArray.append(newArray[count])
            i += 1
        else: i += 1
    

Search()

    
    #print(row)
    #print(row[0:])
    #print(' '.join(row))
