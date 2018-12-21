# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:53:30 2018

@author: alex_s
"""

import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
#memory_usage=otc.info(memory_usage='deep')

uniocc = pd.read_csv('uni.csv', header=None)
uniotc = pd.read_csv('uniotc.csv', header=None)
df1=pd.DataFrame.from_dict(uniocc)

df2=pd.DataFrame.from_dict(uniotc)

df1.columns=['Name']
df2.columns=['Name']
# use fuzz.token_set_ratio or fuzz.token_sort_ratio depending on your needs. See fuzzywuzzy documentation.  
def match(Col1,Col2):
    overall=[]
    score = []
    for n in Col1:
        result=[(fuzz.token_sort_ratio(n, n2),n2) for n2 in Col2 if fuzz.token_sort_ratio(n, n2)> 75]
        if len(result):
            result.sort()    
            print('result {}'.format(result))
            print("Best M={}".format(result[-1][1]))
            overall.append(result[-1][1])
            score.append(result[-1][0])
        else:
            overall.append(" ") 
            score.append(" ")
    #out1 = pd.Series(overall)
    out = pd.DataFrame([overall, score], index=['overall', 'score']).T 
    out.to_csv("out.csv")
    return overall

print(match(df1.Name,df2.Name))
