
# coding: utf-8

# In[9]:

# Load train dataset
from igraph import * 
def load_dataset(g):
    fileNums=[0]
    for i,eachNum in enumerate(fileNums):
        print(eachNum)
        fileName="Datasets/facebook/edges/"+str(eachNum)+".edges"
        print('fileName=',fileName)
        f=open(fileName,'a+')
        nodeID=eachNum
        line=f.readline()
        while(line!=''):
            c=(line.split())
            g=addVertex(g,c[0])
            g=addVertex(g,c[1])
            print('Adding ',c[0],'-->',c[1])
            g.add_edge(c[0],c[1]) 
            line=f.readline()
    g.simplify()    
    return
    
def addVertex(g,name_str):
    try:
        if(name_str not in g.vs['name']):
            print('Inserted node ',name_str)
            g.add_vertex(name=name_str)
        else:
            print ('Node ',name_str,' already present')
            print(g.vs.find(name_str).index)   
    except KeyError:
        g.add_vertex(name=name_str)
    return g
   


def write_tuple_to_file(f,t):
    string=str(t[0])+' '+str(t[1])+'\n'
    f.write(string)

def retrieve_edge_name_tuple(g,t):
    a=(g.vs[t[0]]['name'],g.vs[t[1]]['name'])
    return a



# In[10]:

g=Graph()
# load_dataset(g)


# In[ ]:




# In[3]:

# d=open("Datasets/Self_Datasets/some.txt",'a+')
# d.write('Hello')
# d.close()
# d=open("Datasets/Self_Datasets/some.txt",'a+')
# d.write("sucker")
# d.close()


# In[11]:

import random

def generate_datasets(g,num,train_filename,valid_filename,test_filename):
    load_dataset(g)
    f=open(train_filename,'a+');
    global train_num
    train_num=int(len(g.es)*0.5)
    print('train length=',train_num)
    global test_num
    test_num=int(len(g.es)*0.25)
    global valid_num
    valid_num=int(len(g.es)*0.15)
    print('valid num=',valid_num)
    for i in range(train_num):
        edgeSet=g.es;
        r=random.randint(0,len(edgeSet)-1);
        t=edgeSet[r].tuple
        g.delete_edges(t);
        print('len of es=',len(edgeSet))
        write_tuple_to_file(f,retrieve_edge_name_tuple(g,t))
    f.close()
    f=open(test_filename,'a+');
    for i in range(test_num):
        edgeSet=g.es;
        r=random.randint(0,len(edgeSet)-1);
        print('r=',r)
        t=edgeSet[r].tuple
        g.delete_edges(t);
        print('len of es=',len(edgeSet))
        write_tuple_to_file(f,retrieve_edge_name_tuple(g,t))
    f.close()
    f=open(valid_filename,'a+');
    for i in range(valid_num):
        edgeSet=g.es;
        if(len(g.es)==0):
            break
        else:
            print('len of es=',len(edgeSet))
            r=random.randint(0,len(edgeSet)-1);
            print('r=',r)
            t=edgeSet[r].tuple
            g.delete_edges(t);
            write_tuple_to_file(f,retrieve_edge_name_tuple(g,t))
            if(len(g.es)==0):
                f.close()
                break
    print ('I am done')
    
  
    
        
    


# In[12]:

generate_datasets(g,len(g.es)/10,'Datasets/Self_Datasets/sample_train.edges','Datasets/Self_Datasets/sample_valid.edges','Datasets/Self_Datasets/sample_test.edges')


# In[13]:

# train length=1426 valid=427
print(train_num)


# In[15]:

#Generate negative examples with class label 0.0
mat=g.get_adjacency()

pool_of_empty=list()
count=0
for i,entireNode in enumerate(mat):
    for j,eachVal in enumerate(entireNode):
        if(eachVal==0 and i!=j):
            count+=1;
            pool_of_empty.append((i,j))
print('count=',count)


# In[20]:

# print(pool_of_empty)
for each in pool_of_empty:
    if(each[0]==0):
        pool_of_empty.remove(each)


# In[21]:

import random
def generate_negative_examples(pool,trainfilename,trainnum,validfilename,validnum,testfilename,testnum):
    f=open(trainfilename,'a+')
    for i in range(0,trainnum):
        r=random.randint(0,len(pool)-1);
        t=pool[r];
        pool.remove(t);
        f.write(str(t[0])+' '+str(t[1])+'\n');
    f.close()
    f=open(validfilename,'a+')
    for i in range(0,validnum):
        r=random.randint(0,len(pool)-1);
        t=pool[r];
        pool.remove(t);
        f.write(str(t[0])+' '+str(t[1])+'\n');
    f.close()
    f=open(testfilename,'a+')
    for i in range(0,testnum):
        r=random.randint(0,len(pool)-1);
        t=pool[r];
        pool.remove(t);
        f.write(str(t[0])+' '+str(t[1])+'\n');
    f.close()

        


# In[22]:

generate_negative_examples(pool_of_empty,'Datasets/Self_Datasets/negative_train.edges',train_num,'Datasets/Self_Datasets/negative_valid.edges',valid_num,'Datasets/Self_Datasets/negative_test.edges',test_num)


# In[28]:

#NOT NEEDED

#code to generate the Negative edge graph
from igraph import * 

nodes=set()
fileNums=[0]
for i,eachNum in enumerate(fileNums):
    print(eachNum)
    fileName="Datasets/facebook/edges/"+str(eachNum)+".edges"
    print('fileName=',fileName)
    f=open(fileName)
    nodes.add(eachNum)
    line=f.readline()
    while(line!=''):
        c=line.split()
        nodes.add(c[0])
        print('added ',c[0])
        nodes.add(c[1])
        print('added ',c[1])
        line=f.readline()
    print('Length=',len(nodes))
    print(nodes)
    


# In[ ]:




# In[30]:




# In[ ]:




# In[49]:

print(x.vs[2]['name'])


# In[82]:

print(len(pool_of_empty))
print(type(pool_of_empty))


# In[58]:

print(len(x.vs))
print(334*334)


# In[32]:

print(x.es[0].tuple)


# In[44]:

print(x.vs.find('236').index)


# In[91]:

try:
    print(x.get_eid(x.vs.find('0'),x.vs.find('83'),directed=False))
except InternalError:
    print ("Edge doesnt exist")


# In[30]:

print(type(x.vs))
q=set(x.vs['name'])
print(len(q))
print(len(nodes))
print(q.pop())
print(nodes.pop())


# In[36]:

print(x.get_eid(x.vs.find('236'),x.vs.find('236'),directed=False))

