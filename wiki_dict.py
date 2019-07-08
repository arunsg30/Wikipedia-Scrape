# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 19:57:56 2017

@author: Arun
"""

import requests
import csv
from bs4 import BeautifulSoup

url =  ["https://en.wikipedia.org/wiki/Suncorp_Group",
        "https://en.wikipedia.org/wiki/Thales_Australia",
        "https://en.wikipedia.org/wiki/Woolworths_Limited",
        "https://en.wikipedia.org/wiki/E-Land_Group",
        "https://en.wikipedia.org/wiki/SK_Hynix",
        "https://en.wikipedia.org/wiki/Doosan_Corporation",
        "https://en.wikipedia.org/wiki/Reliance_Industries",
        "https://en.wikipedia.org/wiki/Wipro",
        "https://en.wikipedia.org/wiki/Nippon_Life",
        "https://en.wikipedia.org/wiki/Nippon_Telegraph_and_Telephone",
        "https://en.wikipedia.org/wiki/China_Construction_Bank"]

dic = {}
diclist = {}
for i in range(len(url)):
    html = requests.get(url[i])
    soup = BeautifulSoup(html.content, 'html.parser',from_encoding = 'UTF-8')



    container = soup.find_all("table",{"class":"infobox vcard"})
    
    for j in range(len(container)):    
        tdlist = container[j].find_all('td',{'style':'line-height:1.35em;'})
        thlist = container[j].find_all('th',{'style':'padding-right:0.5em;'})
        if(len(tdlist) == len(thlist)):
            for k in range(len(tdlist)):
                keylist = thlist[k].text.strip()
                print("key list k is "+str(k)+"  ==  "+keylist.strip())
                valuelist = tdlist[k].text.strip()
                print("value list k is "+str(k)+"  ==  "+valuelist)
                dic[keylist] = valuelist
            diclist[url[i]] = dic
            #print(dic["Headquarters"])

    
#with open('dict.csv', 'w',encoding="UTF-8") as csv_file:
#    writer = csv.writer(csv_file)
#    for key, value in dic.items():
#           writer.writerow([key, value])





 
        