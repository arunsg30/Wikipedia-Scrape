# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:47:18 2018

@author: Arun
"""

http://lookup.dbpedia.org/api/search/KeywordSearch?QueryClass=place&QueryString=berlin


import lookup
from bs4 import BeautifulSoup
uri = lookup.get_result('http://lookup.dbpedia.org/api/search/KeywordSearch?QueryClass=place&QueryString=Tata consultancy services')uri = lookup.get_result('http://lookup.dbpedia.org/api/search/KeywordSearch?QueryClass=place&QueryString=TCS')

uri.find('<URI>')
uri



soup = BeautifulSoup(uri, 'html.parser',from_encoding = 'UTF-8') 
container = soup.find_all(<uri>)  

xmlData = '''<Tables>
<Table><Claimable>false</Claimable><MinorRev>80601</MinorRev><Operation>530600 ION MILL</Operation><HTNum>162</HTNum><WaferEC>80318</WaferEC><HolderType>HACARR</HolderType><Job>167187008</Job></Table>
<Table><Claimable>false</Claimable><MinorRev>71115</MinorRev><Operation>530600 ION MILL</Operation><Experiment>6794</Experiment><HTNum>162</HTNum><WaferEC>71105</WaferEC><HolderType>HACARR</HolderType><Job>16799006</Job></Table>
</Tables>
'''

import xml.etree.ElementTree as ET
xml = ET.fromstring(xmlData)

for table in xml.getiterator('Table'):
    for child in table:
        print(child)
        
uri[(uri.index("<URI>")+33):(uri.index("<Description>"))-15]