import os
import sys
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import depth_first_search
from pygraph.algorithms import pagerank

view_dir='/home/ubuntu/linkedin/view/'

gr = digraph() 
cnt=0

def get_otherviewers(fn):
  rc=[]
  with open(fn,'r') as f:
    l=f.readline()
    #print l
    owner,others=l.split(':',1)
    others1=others.split(';')
    for i in xrange(len(others1)/2):
      #print others1[i*2]
      #print others1[i*2].split('/')
      try:
        rc.append(others1[i*2].split('/')[4].split('?')[0])
      except Exception,ex:
        print >> sys.stderr, others
        print >> sys.stderr, ex
  return rc

added_nodes=set([])
added_edges=set([])

for subdir in os.listdir(view_dir):
  for fn in os.listdir(view_dir+subdir):
    #print fn
    key=fn.split('__')[4]
    key=key.split('?')[0]
    #print fn.split('__')
    #print fn,key
    rc=get_otherviewers(view_dir+subdir+'/'+fn)
    try:
      if key not in added_nodes:
        gr.add_node(key)
        added_nodes.add(key)
      for edg in rc:
        if edg not in added_nodes:
          gr.add_node(edg)
          added_nodes.add(edg)
        if (key,edg) not in added_edges:
          gr.add_edge((key,edg))
          added_edges.add((key,edg))
      cnt+=1
      #if cnt>100:break
    except Exception, ex:
      print ex
      print fn

    #def pagerank(graph, damping_factor=0.85, max_iterations=100, min_delta=0.00001):
    pr=pagerank.pagerank(gr, max_iterations=500,min_delta=0.00001)
    
for k in pr:
  print k,pr[k]
