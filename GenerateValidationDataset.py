
# coding: utf-8

# In[1]:

# Load train dataset
from igraph import * 
def load_dataset(g):
    fileNums=[348]
    for i,eachNum in enumerate(fileNums):
        print(eachNum)
        fileName="Datasets/facebook/edges/"+str(eachNum)+".edges"
        print('fileName=',fileName)
        f=open(fileName)
        nodeID=eachNum
        g.add_vertex(name=str(nodeID))
        line=f.readline()
        while(line!=''):
            c=(line.split())
            g=addVertex(g,c[0])
            g=addVertex(g,c[1])
            print('Adding ',c[0],'-->',c[1])
            g.add_edge(c[0],c[1]) 
            print('Adding ',nodeID,'-->',c[0])
            g.add_edge(str(nodeID),c[0])
            print('Adding ',(nodeID),'-->',c[1])
            g.add_edge(str(nodeID),c[1])
            line=f.readline()
        return
    
def addVertex(g,name_str):
    if(name_str not in g.vs['name']):
        print('Inserted node ',name_str)
        g.add_vertex(name=name_str)
    else:
        print ('Node ',name_str,' already present')
        print(g.vs.find(name_str).index)   
    return g
   


# In[2]:

g=Graph()
load_dataset(g)


# In[24]:

edgeSet=g.es
print(len(edgeSet))


# In[25]:

import random

def generate_dataset(g,num,filename):
    f=open(filename,'wr')
    edgeSet=g.es;
    for i in range(num):
        r=random.randint(0,len(edgeSet))
        t=edgeSet[r].tuple
        write_tuple_to_file(f,retrieve_edge_name_tuple(g,t))
    f.close()
        
    


# In[ ]:




# In[26]:

def write_tuple_to_file(f,t):
    string=str(t[0])+' '+str(t[1])+'\n'
    f.write(string)


# In[27]:

def retrieve_edge_name_tuple(g,t):
    a=(g.vs[t[0]]['name'],g.vs[t[1]]['name'])
    return a



# In[28]:




# In[29]:

generate_dataset(g,50,'validation_set.edges')

