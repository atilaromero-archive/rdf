import rdflib

from rdflib import Graph, Literal, BNode, Namespace, RDF
g = Graph()
def printn3(g):
    s = g.serialize(format='n3')
    print s
def printxml(g):
    s = g.serialize(format='xml')
    print s
def printtriples(g):
    # Iterate over triples in store and print them out.
    print("--- printing raw triples ---")
    for s, p, o in g:
        print((s, p, o))

o=Graph()
o.parse('./ontologybbc.ttl',format='n3')
t=Graph()
t.parse('./teste.ttl',format='n3')
n=Graph()
n.parse('./new.ttl',format='n3')
