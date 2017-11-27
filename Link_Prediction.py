
# coding: utf-8

# In[2]:

#Reading input feature values using numpy
import numpy as np
from igraph import *
global num_of_feat
num_of_feat=347


# In[3]:

def load_dataset(fileName,g):
    fileNums=[0]
    for i,eachNum in enumerate(fileNums):
        print(eachNum)
        print('fileName=',fileName)
        f=open(fileName)
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

def load_neg_dataset(fileName,g):
    fileNums=[0]
    for i,eachNum in enumerate(fileNums):
        print(eachNum)
        print('fileName=',fileName)
        f=open(fileName)
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

def load_and_shape_input(file_name):
    a=np.loadtxt(fname=file_name)
    slice_D =[a[i][1:] for i in range(0,num_of_feat)]
    c=np.asarray(slice_D)
    return c

def load_shape_input(file_name_array):
    features=dict()
    for eachname in file_name_array:
        file_name='Datasets/facebook/'+str(eachname)+'.feat'
        a=np.loadtxt(file_name)
        for eachFeat in a:
            features[eachFeat[0]]=np.asarray(eachFeat[1:])
    return features


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




# In[4]:

# Load Feature vectors
li={0}
node_feat=load_shape_input(li)


# In[5]:

g=Graph()
load_dataset('Datasets/Self_Datasets/sample_train.edges',g)


not_g=Graph()
load_dataset('Datasets/Self_Datasets/negative_train.edges',not_g)


# In[6]:

print(type(node_feat))
for eachKey in node_feat.values():
    print(len(eachKey))
    print(type(eachKey))


# In[7]:

# print(node_feat[np.float64(0)])


# In[8]:

# print('positive edges',len(g.es))
# print('negative edges',len(not_g.es))
# t=retrieve_edge_name_tuple(g,(0,1))
# node_feat[np.float64(t[0])]


# In[9]:

def make_class_arrays(g,datalabel):
    output_list=list()
    edgeSet=g.es
    for eachTuple in edgeSet:
        tuple_name=retrieve_edge_name_tuple(g,eachTuple.tuple)
        print('eachTuple=',tuple_name)
        output=np.add(node_feat[np.float64(tuple_name[0])],node_feat[np.float64(tuple_name[1])])
        output_list.append(output)
    return np.asarray(output_list)


# In[10]:

valid_g=Graph()
load_dataset('Datasets/Self_Datasets/sample_valid.edges',valid_g)
# node_feat=load_and_shape_input("Datasets/facebook/0.feat")


valid_not_g=Graph()
load_dataset('Datasets/Self_Datasets/negative_valid.edges',valid_not_g)


# In[11]:

# print(len(node_feat[np.float64(345)]))


# In[12]:

x_positive=make_class_arrays(g,1)
x_negative=make_class_arrays(not_g,1)


# In[13]:

print(x_positive.shape)
print(x_negative.shape)


# In[14]:

valid_x_positive=make_class_arrays(valid_g,1)
valid_x_negative=make_class_arrays(valid_not_g,1)


# In[15]:

print(valid_x_positive.shape)
print(valid_x_negative.shape)


# In[ ]:




# In[16]:

y_positive=np.full(shape=(x_positive.shape[0],1),fill_value=1.0)
y_negative=np.full(shape=(x_negative.shape[0],1),fill_value=0.0)


# In[17]:

print(y_positive.shape)
print(y_negative.shape)


# In[18]:

valid_y_positive=np.full(shape=(valid_x_positive.shape[0],1),fill_value=1.0)
valid_y_negative=np.full(shape=(valid_x_negative.shape[0],1),fill_value=0.0)


# In[19]:

print(valid_x_positive.shape)
print(valid_x_negative.shape)
print(valid_y_positive.shape)
print(valid_y_negative.shape)


# In[20]:

print(valid_y_positive.shape)


# In[21]:

train_X=np.append(x_positive,x_negative,axis=0)
train_Y=np.append(y_positive,y_negative,axis=0)

valid_X=np.append(valid_x_positive,valid_x_negative,axis=0)
valid_Y=np.append(valid_y_positive,valid_y_negative,axis=0)


# In[22]:

print(type(x_positive))
print(valid_X.shape)
print(type(x_negative))
print(valid_Y.shape)
print(type(y_positive))
print(y_positive.shape)
print(train_X.shape)
print(1592+1748)


# In[23]:

from sklearn import linear_model
reg = linear_model.Ridge (alpha = .5)


# In[97]:

# clf.fit(digits.data[:-1], digits.target[:-1])  
reg.fit(X=train_X[:-1],y=train_Y[:-1])


# In[98]:

reg.predict(train_X[-1:])


# In[91]:

len(reg.predict(valid_X))


# In[100]:

np.mean((reg.predict(valid_X)-valid_Y)**2)


# In[24]:

from sklearn.metrics import log_loss
log_loss(valid_Y,reg.predict(valid_X))
# print(0.01)


# In[29]:

from sklearn import svm
clf_svm = svm.SVC()
clf_svm.fit(X=train_X[:-1],y=train_Y[:-1])  


# In[31]:

from sklearn.metrics import log_loss
log_loss(valid_Y,clf_svm.predict(valid_X))


# In[ ]:

from sklearn.neighbors import NearestNeighbors

