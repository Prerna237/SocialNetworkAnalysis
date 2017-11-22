
# coding: utf-8

# In[ ]:

# Add code to visualize the centrality of the graph. Basically this section is to get an idea about the structure of the graph


# In[1]:

from igraph import *
g = Graph()


# In[62]:

def addVertex(g, name_str):
    if(name_str not in g.vs['name']):
        print('Inserted node ', name_str)
        g.add_vertex(name=name_str)
    else:
        print('Node ', name_str, ' already present')
        print(g.vs.find(name_str).index)
    return g


# In[ ]:


# In[63]:

fileNums = [348]
# fileNums=[0]
for i, eachNum in enumerate(fileNums):
    print(eachNum)
    fileName = "Datasets/facebook/edges/" + str(eachNum) + ".edges"
    print('fileName=', fileName)
    f = open(fileName)
    nodeID = eachNum
    g.add_vertex(name=str(nodeID))
    line = f.readline()
    while(line != ''):
        c = (line.split())
        g = addVertex(g, c[0])
        g = addVertex(g, c[1])
        print('Adding ', c[0], '-->', c[1])
        g.add_edge(c[0], c[1])
        print('Adding ', nodeID, '-->', c[0])
        g.add_edge(str(nodeID), c[0])
        print('Adding ', (nodeID), '-->', c[1])
        g.add_edge(str(nodeID), c[1])
        line = f.readline()


# In[64]:

print(len(g.vs))


# In[65]:

def calculate_eigen(g):
    eigen = g.evcent(directed=False)
    for i in range(1, 6):
        maxVal = max(eigen)
        print(i, '==node', g.vs[eigen.index(maxVal)]
              ['name'], ' with score of ', maxVal)
        eigen.remove(maxVal)


# In[66]:

def calculate_closeness(g):
    close = g.closeness(g.vs)
    for i in range(1, 6):
        maxVal = max(close)
        print(i, '==node', g.vs[close.index(maxVal)]
              ['name'], ' with score of ', maxVal)
        close.remove(maxVal)


# In[67]:

def calculate_between(g):
    between = g.betweenness(g.vs)
    for i in range(1, 6):
        maxVal = max(between)
        print(i, '==node', g.vs[between.index(maxVal)]
              ['name'], ' with score of ', maxVal)
        between.remove(maxVal)


# In[68]:

print('Eigen Vector')
calculate_eigen(g)
print('Closeness')
calculate_closeness(g)
print('Betweenness')
calculate_between(g)


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:
