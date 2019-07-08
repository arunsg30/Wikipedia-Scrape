# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 12:24:22 2017

@author: Arun
"""

import requests
from bs4 import BeautifulSoup
#1.Suncorp as sc

#1.sc_Name
print("Suncorp Metway Ltd")

#2.sc_Location
print("Australia and Newzealand")

#sc_Key_people
sc_key_people_url="http://www.suncorpgroup.com.au/about-us/our-leadership-team"
r1=requests.get(sc_key_people_url)
soup1=BeautifulSoup(r1.content)
sc_key_people=soup1.find_all("h2")
jobtitle=soup1.find_all("div",{"id":"leader_job_title"})
sc_key_people_list=[]
sc_key_people_title = []
for i in sc_key_people:
   sc_key_people_list.append(i.text.strip())
for i in jobtitle:
    sc_key_people_title.append(i.text.strip())
    
sc_key_people_nametitle = []
if(len(sc_key_people_list) == len(sc_key_people_title)):
    for i in range(len(sc_key_people_list)):
        sc_key_people_nametitle.append(sc_key_people_list[i]+", "+sc_key_people_title[i])
   
#Contact Info
sc_contact_url="http://www.suncorpgroup.com.au/contact-us"
r2=requests.get(sc_contact_url)
soup2=BeautifulSoup(r2.content)
sc_contact_us=soup2.find_all("a",{"href":"mailto:direct@suncorp.com.au"})
sc_contact_mail=[]
for i in sc_contact_us:
    sc_contact_mail=(i["href"])

#about_us
sc_about_us_url="http://www.suncorpgroup.com.au/about-us/who-we-are"
r3=requests.get(sc_about_us_url)
soup3=BeautifulSoup(r3.content)
sc_about_us=soup3.find_all("div",{"class":"region region-content"})
sc_about_us_list=[]
for i in sc_about_us:
   sc_about_us_list.append(i.text.strip())

#News and Media
sc_news_url="http://www.suncorpgroup.com.au/media/news"
r4=requests.get(sc_news_url)
soup4=BeautifulSoup(r4.content)
sc_news=soup4.find_all("h2")
news_list=[]
for i in sc_news:
    news_list.append(i.text.strip())
    
#subsidaries
sc_subsidaries_url="http://www.suncorpgroup.com.au/about-us/what-we-do/our-brands"
r5=requests.get(sc_subsidaries_url)
soup5=BeautifulSoup(r5.content)
sc_subsidaries_container=soup5.find_all("div",{"class":"field-item even"})
sc_subsidaries_container2=sc_subsidaries_container[2].find_all("a")
sc_subsidaries_list=[]
import re

for i in sc_subsidaries_container2:
    img=i.find("img")
    #print(img['alt'])
    #re_pattern=re.match(r"(.*)(\s[l][o][g][o])",img['alt'],re.M|re.I)
    re_pattern = re.match(r'(.*)(\s[l][o][g][o])',img['alt'])
    if(re_pattern):
        print(re_pattern.group(1))
    sc_subsidaries_list.append(i.text.strip())
    

#Career Opportunity

#######################################################################
#2.Thales as th

import requests
from bs4 import BeautifulSoup

#1.th_Name
print("Thales Australia Limited")

#2.th_Location
print("Australia and Newzealand")

#th_Key_people
th_key_people_url="https://www.thalesgroup.com/en/global/about-us#board-directors"
r6=requests.get(th_key_people_url)
soup6=BeautifulSoup(r6.content)
th_key_people=soup6.find_all("div",{"class":"peoples__list__item__info"})
th_key_people_list=[]
for i in th_key_people:
   th_key_people_list.append(i.h5.text.strip())

#Contact Info
th_contact_url="https://www.thalesgroup.com/en/countries/asia-pacific/australia#contact"
r7=requests.get(th_contact_url)
soup7=BeautifulSoup(r7.content)
th_contact_info=soup6.find("div",{"class","brick__contacts__bloc__phone"})
th_contact_phone=(th_contact_info.text.strip())

#about_us
th_aboutus_url="https://www.thalesgroup.com/en/countries/asia-pacific/australia"
r8=requests.get(th_aboutus_url)
soup8=BeautifulSoup(r8.content)
th_aboutus=soup8.find("div",{"class","field__item even"})
for i in th_aboutus:
    th_aboutus_list=i

#News and Media
th_news_url="https://www.thalesgroup.com/en/search-everything/all/"
r9=requests.get(th_news_url)
soup9=BeautifulSoup(r9.content)
th_news=soup9.find_all("div",{"class":"big__list__item__info"})
th_news_list = []
for i in th_news:
    th_news_list.append(i.h5.text)

th_career_url="https://jobs.thalesgroup.com/search-jobs"
r10=requests.get(th_career_url)
soup10=BeautifulSoup(r10.content)
th_careers=soup10.find("section",{"id":"search-results-list"})#,{"id","search-results-list"})
th_careers1=th_careers.find_all("ul")
th_careers2 = th_careers1[1]
th_careers_list = []
lid = th_careers2.find_all('li')
for i in lid:
    th_careers_list.append(i.h2.text.strip())


    
#subsidaries
#sc_subsidaries_url="http://www.suncorpgroup.com.au/about-us/what-we-do/our-brands"
#r5=requests.get(sc_subsidaries_url)
#soup5=BeautifulSoup(r5.content)
#sc_subsidaries_container=soup5.find_all("div",{"class":"field-item even"})
#sc_subsidaries_list=[]
#for i in sc_subsidaries_container:
#    sc_subsidaries_container.find("h2")
#    sc_subsidaries_list.append(i.text.strip())
#######################################################################
   
#3.Woolworths Limited as ww  
import requests
from bs4 import BeautifulSoup

#1.ww_Name
print("Woolworths Limited")

#2.ww_Location
print("Australia and Newzealand")

#sc_Key_people
ww_key_people_url="https://www.woolworthsgroup.com.au/page/about-us/our-leadership-team/board-of-directors/"
r12=requests.get(ww_key_people_url)
soup12=BeautifulSoup(r12.content)
ww_key_people=soup12.find("div",{"class":"news"})
ww_key_people1=ww_key_people.find_all("h4")
ww_key_people_list=[]
for i in ww_key_people1:
   ww_key_people_list.append(i.text.strip())

   
#ww_Contact Info
ww_contact_url="https://www.woolworthsgroup.com.au/page/contact-us/contact-information/"
r13=requests.get(ww_contact_url)
soup13=BeautifulSoup(r13.content)
ww_contact_us=soup13.find("div",{"class":"contact-info__block--phone"})
#ww_contact_us1=ww_contact_us.find("br")
for i in ww_contact_us:
    ww_contact_num=i

#about_us
ww_about_us_url="https://www.woolworthsgroup.com.au/page/about-us/"
r14=requests.get(ww_about_us_url)
soup14=BeautifulSoup(r14.content)
ww_about_us=soup14.find("div",{"class":"cms-content"})
ww_about_us_list=ww_about_us.text.strip()
#sc_about_us_list=[]
#for i in sc_about_us:
#   sc_about_us_list.append(i.text.strip())

#News and Media
ww_news_url="https://www.woolworthsgroup.com.au/page/media/"
r15=requests.get(ww_news_url)
soup15=BeautifulSoup(r15.content)
ww_news=soup15.find_all("h4",{"class":"news__heading"})
ww_news_list=[]
for i in ww_news:
    ww_news_list.append(i.text.strip())
    
#subsidaries
#ww_subsidaries_url="https://www.woolworthsgroup.com.au/page/about-us/our-brands/"
#r16=requests.get(ww_subsidaries_url)
#soup5=BeautifulSoup(r5.content)
#sc_subsidaries_container=soup5.find_all("div",{"class":"field-item even"})
#sc_subsidaries_container2=sc_subsidaries_container[2].find_all("a")
#sc_subsidaries_list=[]
#import re
#
#for i in sc_subsidaries_container2:
#    img=i.find("img")
#    #print(img['alt'])
#    #re_pattern=re.match(r"(.*)(\s[l][o][g][o])",img['alt'],re.M|re.I)
#    re_pattern = re.search(r'(.*)(\s[l][o][g][o])',img['alt'])
#    
#    print(re_pattern.group(1))
#    sc_subsidaries_list.append(i.text.strip())
    

#Career Opportunity
ww_careeers_url="https://www.wowcareers.com.au/jobs/listing?query=&refine_requisition_number=&brand=&state=&country=&refine_posted_within=&expertise=&worktype=&postcode=&location_within=&role="
r17=requests.get(ww_careeers_url)
soup17=BeautifulSoup(r17.content)
ww_careers_container = soup17.find_all("ul",{"class":"jobs__listing"})
ww_careeers=ww_careers_container.find("h3",{"class":"jobs__listing-item-title"})
ww_careeers1=ww_careeers.find("a")
ww_careers_list = []
for i in ww_careeers1:
    ww_careers_list.append(i.text.strip())
    print(ww_careers_list)
ww_careers_list1 = []
for i in ww_careers1:
    ww_careers_list1.append(i.a)
    

##########################################################################
#2.China Construction Bank Corporation as ccb

import requests
from bs4 import BeautifulSoup

#1.ccb_Name
print("China Construction Bank Corporation")

#2.th_Location
print("China")

##th_Key_people
#ccb_key_people_url="https://www.thalesgroup.com/en/global/about-us#board-directors"
#r6=requests.get(th_key_people_url)
#soup6=BeautifulSoup(r6.content)
#th_key_people=soup6.find_all("div",{"class":"peoples__list__item__info"})
#th_key_people_list=[]
#for i in th_key_people:
#   th_key_people_list.append(i.h5.text.strip())

#Contact Info
th_contact_url="https://www.thalesgroup.com/en/countries/asia-pacific/australia#contact"
r7=requests.get(th_contact_url)
soup7=BeautifulSoup(r7.content)
th_contact_info=soup6.find("div",{"class","brick__contacts__bloc__phone"})
th_contact_phone=(th_contact_info.text.strip())

#about_us
th_aboutus_url="https://www.thalesgroup.com/en/countries/asia-pacific/australia"
r8=requests.get(th_aboutus_url)
soup8=BeautifulSoup(r8.content)
th_aboutus=soup8.find("div",{"class","field__item even"})
for i in th_aboutus:
    th_aboutus_list=i

#News and Media
th_news_url="https://www.thalesgroup.com/en/search-everything/all/"
r9=requests.get(th_news_url)
soup9=BeautifulSoup(r9.content)
th_news=soup9.find_all("div",{"class":"big__list__item__info"})
th_news_list = []
for i in th_news:
    th_news_list.append(i.h5.text)

th_career_url="https://jobs.thalesgroup.com/search-jobs"
r10=requests.get(th_career_url)
soup10=BeautifulSoup(r10.content)
th_careers=soup10.find("section",{"id":"search-results-list"})#,{"id","search-results-list"})
th_careers1=th_careers.find_all("ul")
th_careers2 = th_careers1[1]
th_careers_list = []
lid = th_careers2.find_all('li')
for i in lid:
    th_careers_list.append(i.h2.text.strip())


    
#subsidaries
#sc_subsidaries_url="http://www.suncorpgroup.com.au/about-us/what-we-do/our-brands"
#r5=requests.get(sc_subsidaries_url)
#soup5=BeautifulSoup(r5.content)
#sc_subsidaries_container=soup5.find_all("div",{"class":"field-item even"})
#sc_subsidaries_list=[]
#for i in sc_subsidaries_container:
#    sc_subsidaries_container.find("h2")
#    sc_subsidaries_list.append(i.text.strip())
##########################################################################################

import requests
from bs4 import BeautifulSoup
#1.e-land fashion china as elfc

#1.sc_Name
print("e-land fashion china")

#2.sc_Location
print("China")

#sc_Key_people
elfc_key_people_url="http://www.elandfashionchina.com/en_company4.php"
r18=requests.get(elfc_key_people_url)
soup18=BeautifulSoup(r18.content)
elfc_key_people_container=soup18.find("div",{"id":"contxt"})
tdlist=elfc_key_people_container.findAll("td",{"class":"contxt_txt"})
elfc_key_people = []
for i in tdlist:
    elfc_key_people.append(i.text.strip())
    
   
#Contact Info
elfc_contact_url="http://www.elandfashionchina.com/en_contact.php"
r19=requests.get(elfc_contact_url)
soup19=BeautifulSoup(r19.content)
elfc_contact_us=soup19.find_all("span",{"class":"contxt_txt"})
elfc_contact_details=[]
for i in elfc_contact_us:
    elfc_contact_details.append(i.text.strip())

#about_us
elfc_about_us_url="http://www.elandfashionchina.com/en_company1.php"
r20=requests.get(elfc_about_us_url)
soup20=BeautifulSoup(r20.content)
elfc_about_us=soup20.find("p",{"class":"contxt_txt"})
elfc_about_us_list = []
elfc_about_us_list.append(elfc_about_us)

#News and Media
#elfc_news_url="http://www.elandfashionchina.com/en_newsroom1.php"
#r21=requests.get(elfc_news_url)
#soup21=BeautifulSoup(r21.content)
#elfc_news=soup21.find_all("h2")
#news_list=[]
#for i in sc_news:
#    news_list.append(i.text.strip())
    
#subsidaries
elfc_subsidaries_url="http://www.elandfashionchina.com/en_brand3.php"
r22=requests.get(elfc_subsidaries_url)
soup22=BeautifulSoup(r22.content)
elfc_subsidaries_container=soup22.find("div",{"id":"leftmenu"})
elfc_subsidaries=elfc_subsidaries_container.find_all("li")
elfc_subsidaries_list = []
for i in elfc_subsidaries:
    elfc_subsidaries_list.append(i.text.strip())

#############################################################################

#6.Doosan corporation  as dc  
import requests
from bs4 import BeautifulSoup

#1.dc_Name
print("Doosan Corporation")

#2.dc_Location
print("Korea")

#dc_Key_people
dc_key_people_url="http://www.doosan.com/en/intro/leadership/directors/"
r23=requests.get(dc_key_people_url)
soup23=BeautifulSoup(r23.content)
dc_key_people=soup23.find("div",{"class":"contents-wrap leadership directors"})
dc_key_people_dict = {}
for j in range(len(dc_key_people)):
        tdlist = dc_key_people[j].find_all('td')
        thlist = dc_key_people[j].find_all('tr')
        if(len(tdlist) == len(thlist)):
            for k in range(len(tdlist)):
                keylist = thlist[k].text.strip()
                print("key list k is "+str(k)+"  ==  "+keylist.strip())
                valuelist = tdlist[k].text.strip()
                print("value list k is "+str(k)+"  ==  "+valuelist)
                dc_key_people_dict[keylist] = valuelist
   
#dc_Contact Info
ww_contact_url="https://www.woolworthsgroup.com.au/page/contact-us/contact-information/"
r13=requests.get(ww_contact_url)
soup13=BeautifulSoup(r13.content)
ww_contact_us=soup13.find("div",{"class":"contact-info__block--phone"})
#ww_contact_us1=ww_contact_us.find("br")
for i in ww_contact_us:
    ww_contact_num=i

#about_us
ww_about_us_url="https://www.woolworthsgroup.com.au/page/about-us/"
r14=requests.get(ww_about_us_url)
soup14=BeautifulSoup(r14.content)
ww_about_us=soup14.find("div",{"class":"cms-content"})
ww_about_us_list=ww_about_us.text.strip()
#sc_about_us_list=[]
#for i in sc_about_us:
#   sc_about_us_list.append(i.text.strip())

#News and Media
dc_news_url="http://www.doosan.com/en/media/news/"
r101=requests.get(dc_news_url)
soup101=BeautifulSoup(r101.content)
dc_news=soup101.find("ul")
dc_news1=dc_news.find_all("li")
dc_news2=dc_news1.find("h2")
dc_news_list=[]
for i in dc_news2:
    print(i.a.text)# not working
    
#subsidaries
dc_subsidaries_url="http://www.doosan.com/en/intro/affiliate/"
r100=requests.get(dc_subsidaries_url)
soup100=BeautifulSoup(r100.content)
dc_subsidaries_container=soup100.find("ul",{"class":"type-accordion web-except"})
dc_subsidaries_container2=dc_subsidaries_container.find_all("a")
dc_subsidaries_list=[]
for i in dc_subsidaries_container2:
    a=i.text.strip()
    if a:
       dc_subsidaries_list.append(i.text.strip())
       
###########################################################################################

#3.NTT Communications Corporation Limited as nttc 
import requests
from bs4 import BeautifulSoup

#1.ww_Name
print("NTT Communications Corporation")

#2.ww_Location
print("Japan")

#sc_Key_people
ww_key_people_url="http://www.ntt.com/en/about-us/company-profile/board.html"
r12=requests.get(ww_key_people_url)
soup12=BeautifulSoup(r12.content)
ww_key_people=soup12.find("div",{"class":"news"})
ww_key_people1=ww_key_people.find_all("h4")
ww_key_people_list=[]
for i in ww_key_people1:
   ww_key_people_list.append(i.text.strip())

   
#ww_Contact Info
ww_contact_url="https://www.woolworthsgroup.com.au/page/contact-us/contact-information/"
r13=requests.get(ww_contact_url)
soup13=BeautifulSoup(r13.content)
ww_contact_us=soup13.find("div",{"class":"contact-info__block--phone"})
#ww_contact_us1=ww_contact_us.find("br")
for i in ww_contact_us:
    ww_contact_num=i

#about_us
ww_about_us_url="http://www.ntt.com/en/about-us.html"
r14=requests.get(ww_about_us_url)
soup14=BeautifulSoup(r14.content)
ww_about_us=soup14.find("div",{"class":"cms-content"})
ww_about_us_list=ww_about_us.text.strip()
#sc_about_us_list=[]
#for i in sc_about_us:
#   sc_about_us_list.append(i.text.strip())

#News and Media
ww_news_url="https://www.woolworthsgroup.com.au/page/media/"
r15=requests.get(ww_news_url)
soup15=BeautifulSoup(r15.content)
ww_news=soup15.find_all("h4",{"class":"news__heading"})
ww_news_list=[]
for i in ww_news:
    ww_news_list.append(i.text.strip())
    
#subsidaries
#ww_subsidaries_url="https://www.woolworthsgroup.com.au/page/about-us/our-brands/"
#r16=requests.get(ww_subsidaries_url)
#soup5=BeautifulSoup(r5.content)
#sc_subsidaries_container=soup5.find_all("div",{"class":"field-item even"})
#sc_subsidaries_container2=sc_subsidaries_container[2].find_all("a")
#sc_subsidaries_list=[]
#import re
#
#for i in sc_subsidaries_container2:
#    img=i.find("img")
#    #print(img['alt'])
#    #re_pattern=re.match(r"(.*)(\s[l][o][g][o])",img['alt'],re.M|re.I)
#    re_pattern = re.search(r'(.*)(\s[l][o][g][o])',img['alt'])
#    
#    print(re_pattern.group(1))
#    sc_subsidaries_list.append(i.text.strip())
    

#Career Opportunity
ww_careeers_url="https://www.wowcareers.com.au/jobs/listing?query=&refine_requisition_number=&brand=&state=&country=&refine_posted_within=&expertise=&worktype=&postcode=&location_within=&role="
r17=requests.get(ww_careeers_url)
soup17=BeautifulSoup(r17.content)
ww_careers_container = soup17.find_all("ul",{"class":"jobs__listing"})
ww_careeers=ww_careers_container.find("h3",{"class":"jobs__listing-item-title"})
ww_careeers1=ww_careeers.find("a")
ww_careers_list = []
for i in ww_careeers1:
    ww_careers_list.append(i.text.strip())
    print(ww_careers_list)
ww_careers_list1 = []
for i in ww_careers1:
    ww_careers_list1.append(i.a)
    
######################################################################################
#6.Doosan corporation  as dc  
import requests
from bs4 import BeautifulSoup

#1.dc_Name
print("Doosan Corporation")

#2.dc_Location
print("Korea")

#dc_Key_people
dc_key_people_url="http://www.doosan.com/en/intro/leadership/directors/"
r23=requests.get(dc_key_people_url)
soup23=BeautifulSoup(r23.content)
dc_key_people=soup23.find("div",{"class":"contents-wrap leadership directors"})
dc_key_people_dict = {}
for j in range(len(dc_key_people)):
        tdlist = dc_key_people[j].find_all('td')
        thlist = dc_key_people[j].find_all('tr')
        if(len(tdlist) == len(thlist)):
            for k in range(len(tdlist)):
                keylist = thlist[k].text.strip()
                print("key list k is "+str(k)+"  ==  "+keylist.strip())
                valuelist = tdlist[k].text.strip()
                print("value list k is "+str(k)+"  ==  "+valuelist)
                dc_key_people_dict[keylist] = valuelist
   
#dc_Contact Info
ww_contact_url="https://www.woolworthsgroup.com.au/page/contact-us/contact-information/"
r13=requests.get(ww_contact_url)
soup13=BeautifulSoup(r13.content)
ww_contact_us=soup13.find("div",{"class":"contact-info__block--phone"})
#ww_contact_us1=ww_contact_us.find("br")
for i in ww_contact_us:
    ww_contact_num=i

#about_us
ww_about_us_url="https://www.woolworthsgroup.com.au/page/about-us/"
r14=requests.get(ww_about_us_url)
soup14=BeautifulSoup(r14.content)
ww_about_us=soup14.find("div",{"class":"cms-content"})
ww_about_us_list=ww_about_us.text.strip()
#sc_about_us_list=[]
#for i in sc_about_us:
#   sc_about_us_list.append(i.text.strip())

#News and Media
dc_news_url="http://www.doosan.com/en/media/news/"
r101=requests.get(dc_news_url)
soup101=BeautifulSoup(r101.content)
dc_news=soup101.find("ul")
dc_news1=dc_news.find_all("li")
dc_news2=dc_news1.find("h2")
dc_news_list=[]
for i in dc_news2:
    print(i.a.text)# not working
    
#subsidaries
dc_subsidaries_url="http://www.doosan.com/en/intro/affiliate/"
r100=requests.get(dc_subsidaries_url)
soup100=BeautifulSoup(r100.content)
dc_subsidaries_container=soup100.find("ul",{"class":"type-accordion web-except"})
dc_subsidaries_container2=dc_subsidaries_container.find_all("a")
dc_subsidaries_list=[]
for i in dc_subsidaries_container2:
    a=i.text.strip()
    if a:
       dc_subsidaries_list.append(i.text.strip())
       
       
     #################################################
     
     
#6.Reliance Industris   as RI 
import requests
from bs4 import BeautifulSoup

#1.dc_Name
print("Reliance Industries")

#2.dc_Location
print("India")

#dc_Key_people
RI_key_people_url="http://www.ril.com/OurCompany/Leadership/BoardOfDirectors.aspx"
r200=requests.get(RI_key_people_url)
soup200=BeautifulSoup(r200.content)
RI_key_people=soup200.find("div",{"class":"row board-directors-list-sec pB30"})
RI_key_people1=RI_key_people.find_all("img")

RI_key_people_list = []
for i in RI_key_people1:
    print(i)
    RI_key_people_list.append(i["alt"])
    
   
#RI_Contact Info
ww_contact_url="https://www.woolworthsgroup.com.au/page/contact-us/contact-information/"
r13=requests.get(ww_contact_url)
soup13=BeautifulSoup(r13.content)
ww_contact_us=soup13.find("div",{"class":"contact-info__block--phone"})
#ww_contact_us1=ww_contact_us.find("br")
for i in ww_contact_us:
    ww_contact_num=i

RI_about_us_url="http://www.ril.com/OurCompany/About.aspx"
r201=requests.get(RI_about_us_url)
soup201=BeautifulSoup(r201.content)
RI_about_us=soup201.find("p",{"class":"mT10"})
RI_about_us_list=RI_about_us.text.strip()
#sc_about_us_list=[]
#for i in sc_about_us:
#   sc_about_us_list.append(i.text.strip())

#News and Media
RI_news_url="http://www.doosan.com/en/media/news/"
r101=requests.get(dc_news_url)
soup101=BeautifulSoup(r101.content)
dc_news=soup101.find("ul")
dc_news1=dc_news.find_all("li")
dc_news2=dc_news1.find("h2")
dc_news_list=[]
for i in dc_news2:
    print(i.a.text)# not working
    
#subsidaries
dc_subsidaries_url="http://www.doosan.com/en/intro/affiliate/"
r100=requests.get(dc_subsidaries_url)
soup100=BeautifulSoup(r100.content)
dc_subsidaries_container=soup100.find("ul",{"class":"type-accordion web-except"})
dc_subsidaries_container2=dc_subsidaries_container.find_all("a")
dc_subsidaries_list=[]
for i in dc_subsidaries_container2:
    a=i.text.strip()
    if a:
       dc_subsidaries_list.append(i.text.strip())
    