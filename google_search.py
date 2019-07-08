#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:20:36 2017

@author: arunsugumar
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

data_set = pd.read_excel("citrix_Cust.xlsx")
data = data_set["ENDUSER_NAME"]
data =  data.values.tolist()
url_list = []
no_url = []
for i in range(len(data)):
    try:
        print("yes")
        research_later = data[i]+" webiste"
        goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + research_later
        r = requests.get(goog_search)
        soup = BeautifulSoup(r.text, "html.parser")
        url_list.append(soup.find('cite').text)
        print(i)
    except Exception as e:
        print("NO")
        no_url.append(data[i])
        
for i in url_list:
    if "https://" not in i:
        i = "https://"+str(i)
names = []
for i in range(len(url_list)):
    try:
         name = re.findall(r'(\\*[A-Z]\w+)', str(url_list[i]), re.I|re.M)
         names.append(name[name.index('wiki')+1:])
    except Exception as e:
        if str(e) == "'wiki' is not in list":
            print("yes")
            names.append(['No_wiki'])
        else:
            pass
names = [j for i in names for j in i]
#     name = name[-1]
#     name=name.replace("_"," ")
#     names.append(name)
df = pd.DataFrame(names)
df.to_excel("14-feb-2018.xlsx")
