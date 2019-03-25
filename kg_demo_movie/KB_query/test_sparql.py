#!/usr/bin/python
# coding:utf-8
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://localhost:2020/sparql")
sparql.setQuery("""
    PREFIX : <http://www.kgdemo.com#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT ?n WHERE {
      ?s rdf:type :Person.
      ?s :personName '巩俐'.
      ?s :hasActedIn ?o.
      ?o :movieTitle ?n.
      ?o :movieRating ?r.
    FILTER (?r >= 7)
    }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["n"]["value"])
