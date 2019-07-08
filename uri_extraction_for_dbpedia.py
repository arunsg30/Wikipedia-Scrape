#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:02:55 2017

@author: arunsugumar
"""

import re
import requests
from bs4 import BeautifulSoup
#from mediawiki import MediaWiki
import wikipedia
import pandas as pd


data = pd.read_excel("Customer_List.xlsx")
org_id = data['ENDUSER_ORG_ID']
org_id = org_id.values.tolist()
company_name = data['ENDUSER_NAME']
company_name = company_name.values.tolist()

no_page_list = []
page_list = []
check = []
url_mediawiki = []
for i in range(len(company_name)):
    print(i)
    try:
              page = wikipedia.page(company_name[i])
              url_mediawiki.append(page.url) 
#              page_list.append(company_name[i])
    except:
              url_mediawiki.append(company_name[i])
    


import pandas as pd

#
## # writing to a csv file
#df = pd.DataFrame({'a':range(10)})
#df['org_id'] = pd.Series(org_id, index = df.index[:len(org_id)])
#df['company_name'] = pd.Series(company_name, index = df.index[:len(company_name)]) 
#df['url'] =  pd.Series(url_mediawiki, index = df.index[:len(url_mediawiki)])
#print (df)
#



  

percentile_list = pd.DataFrame(
    {'lst1Title': org_id,
     'lst2Title': company_name
    })
df = pd.DataFrame(url_mediawiki)
#df2 = df.transpose()
df.to_excel("c360_23-march.xlsx")
print("written")







