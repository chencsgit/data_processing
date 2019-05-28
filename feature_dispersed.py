# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:25:34 2019

@author: chuze
"""


import requests

from bs4 import BeautifulSoup 
import json
import re
import pandas as pd
import numpy as np
from time import sleep

from os import listdir
import os, sys

import nltk
from newspaper import Article
from geograpy.utils import remove_non_ascii

address = 'C:/Users/chuze/Desktop/weicheche/2019IJCAI_DTTF/'




e = pd.read_csv('%sUserSide.csv'%address,encoding = "utf-8") 

l = e['11']


cityl= []
for i in range(len(l)):
        
    text = l[i]
    try:
        text = text.replace(',',' ')
        text = text.replace('/',' ')
        text = text.replace('-',' ')
        text = nltk.word_tokenize(remove_non_ascii(text))
        cityl = cityl + (text)
    except:
        1
        

citySet = list(set(cityl))
    
count = np.zeros(len(citySet))

for i in range(len(l)):
        
    text = l[i]
    try:
        text = text.replace(',',' ')
        text = text.replace('/',' ')
        text = text.replace('-',' ')
        text = nltk.word_tokenize(remove_non_ascii(text))
        for j in text:
            count[citySet.index(j)] +=1
    
    except:
        1
    #try:

cityE = []

for i in range(len(l)):
    text = l[i]
    try:
        text = text.replace(',',' ')
        text = text.replace('/',' ')
        text = text.replace('-',' ')

        text = nltk.word_tokenize(remove_non_ascii(text))
        if len(text) ==1:
            
            
            cityE.append(citySet.index(text[0]))
        else:
            maxNum = 0
            maxC = 0
            for j in text:
                if count[citySet.index(j)] > maxNum:
                    maxNum = count[citySet.index(j)]
                    maxC = citySet.index(j)
            cityE.append(maxC)
    except:
        cityE.append(-1)


tempset = list(set(cityE))
tempset.remove(-1)
cityC = []


for i in range(len(cityE)):
    if cityE[i] == -1:
        cityC.append(-1)
    else:
        cityC.append(tempset.index(cityE[i]))        

sideM = pd.DataFrame(cityC)   
sideM.to_csv('%sStyleUserSide.csv'%address,index = False,encoding = "utf-8")
e = pd.read_csv('%sStyleUserSide.csv'%address,encoding = "utf-8") 
        




       