"
Created on Mon Sep 18 11:53:30 2017

@author: arunsugumar
"""
# importing necessary libraries
import pandas as pd
import string
import re
import requests
from bs4 import BeautifulSoup

# words to remove
junk_words = ['ltd.','ltd','inc','co.','co','limited','pty','pty.','inc.','co.,']+[string.punctuation]


#creating dataframe
#name = pd.read_excel("su.xlsx")
#page = name.iloc[0:100,1]

page = ["Queanbeyan_city_council","Thales_Australia","Woolworths_Limited","E-Land_Group","SK_Hynix","Doosan_Corporation","Reliance_Industries","Wipro","Nippon_Life","Nippon_Telegraph_and_Telephone","China_Construction_Bank"]
#compamny_list = []      
#for i in range(len(page)):
#    compamny_list.append([str(page[i]).lower()])
#    print(compamny_list)
#    print(len(compamny_list))
#    
## wiki_list = []
## for i in compamny_list:
##     for j in i:
##         wiki_list.append(j.split(sep=" "))
#        
#        
## company_name_cleaned= []        
## for k in range(len(wiki_list)):
##     temp = []
##     for l in range(len(wiki_list[k])):
##         if wiki_list[k][l] not in junk_words and string.punctuation:
##             temp.append(wiki_list[k][l])
##     company_name_cleaned.append(temp)
## #    print(company_name_cleaned)
#    
## url_for_wiki = []   
## name_for_search = [] 
## for k in range(len(company_name_cleaned)):
##             a = "_".join(company_name_cleaned[k])
##             c = " ".join(company_name_cleaned[k])
## #            print(a)
##             url_for_wiki.append(a)
##             name_for_search.append(c)

# from mediawiki import MediaWiki
# wikipedia = MediaWiki()
# no_page_list = []
# page_list = []
# check = []
# for i in range(len(name_for_search)):
#     print(i)
#     try:
#               page = wikipedia.page(name_for_search[i])
#               print('******')
#               print(page)
#               print(name_for_search[i])
#               page_list.append(name_for_search[i])
#     except:
#         no_page_list.append(name_for_search[i])
           

   

# ###################################################

# #parsing by url
# url =  []
# for i in range(len(page_list)):
#     url.append("https://en.wikipedia.org/wiki/"+page_list[i])
# #    print(url)


# names = []
# for i in range(len(url)):
#     name = re.findall(r'(\\*[A-Z]\w+)', url[i], re.I|re.M)
#     name = name[5]
#     name=name.replace("_"," ")
#     names.append(name)
    

# diclist = {}
# for i in range(len(url)):
#     html = requests.get(url[i])
#     print(html)
#     soup = BeautifulSoup(html.content, 'html.parser',from_encoding = 'UTF-8') 
#     container = soup.find_all("table",{"class":"infobox vcard"})  
#     if container == []:
#         print(url[i])
        
   
#     for j in range(len(container)):  
#         print(j)
#         tdlist = container[j].find_all('td',{'style':'line-height:1.35em;'})
#         thlist = container[j].find_all('th',{'style':'padding-right:0.5em;'})
#         if(len(tdlist) == len(thlist)):
#             dic = {}
#             for k in range(len(tdlist)):
#                 keylist = thlist[k].text.strip()
#                 valuelist = tdlist[k].text.strip()
#                 dic[keylist] = valuelist
#                 print(i)
#             diclist[names[i]] = dic



# # writing to a csv file
