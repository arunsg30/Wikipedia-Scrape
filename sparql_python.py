#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:20:36 2017

@author: arunsugumar
"""
import pandas as pd


data_set = pd.read_excel("intern_filtered_data.xlsx")
org_id = data_set['ENDUSER_ORG_ID'];org_id = org_id.tolist()
enduser_name = data_set['ENDUSER_NAME'];enduser_name = enduser_name.tolist()
wiki_url = data_set['URL'];wiki_url = wiki_url.tolist()
uri = data_set['URI'];uri = uri.tolist()
a
ans = []
from SPARQLWrapper import SPARQLWrapper, JSON
for i in range(10):
    try:
       sparql = SPARQLWrapper("http://dbpedia.org/sparql")
       sparql.setQuery("""PREFIX dbp: <http://dbpedia.org/property/>
       PREFIX dbo: <http://dbpedia.org/ontology/>
       PREFIX res: <http://dbpedia.org/resource/>
       PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
       PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
       SELECT DISTINCT  ?uri ?PK_ID ?CompanyName ?OPERATING_INCOME ?PROFIT ?REVENUE_OTHER  ?Location
       {
              ?uri rdf:type dbo:Company.
              optional{?uri dbo:wikiPageID ?PK_ID}
              optional{?uri dbo:location ?Location}
              optional{?uri rdfs:label ?CompanyName.}
              optional{?uri dbp:revenue ?REVENUE_OTHER}
              optional{?uri dbp:profit ?PROFIT}
              optional{?uri dbo:operatingIncome ?OPERATING_INCOME}
              FILTER ( lang(?CompanyName) = "en" && regex(?uri,"""+"\""+str(uri[i])+"\""+""", "i"))
       }      
       """)
       sparql.setReturnFormat(JSON)
       results = sparql.query().convert()
       ans.append(results)
    except Exception as e:
        pass
print(ans)

