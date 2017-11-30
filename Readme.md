# Social Networks: Link Prediction

### Capstone Project: Data and Knowledge Engineering

#### Video link:  [Social Network Analysis: Link Prediction](https://youtu.be/XRMhgxW-C_M)

---

### ✨Contributors: Group 1✨

- Pranjal Mathur  (1410110296) 
- Prerna (1410110306)
- Saketh Vallakatla (1410110352)

------

## Problem Statement

> Given an instance of set of nodes (users) in a social network graph, the aim is to find the influencing (important) users and to predict the likelihood of a future association (edge) between two nodes, knowing that there is no association between the nodes in the current state of the graph.


## Motivation
The edges described in the problem statement could be of any form: friendship, collaboration, following or mutual interests. Here, we specifically study and build our model over Facebook's social network, with the following areas of motivation:

* General application of friends recommendation to a particular user.
* Predicting hidden links in a social network group formed by terrorists along with identification of their leaders/ key influencers.
* Targeted marketing of products: Marketing through highly influential individuals and also identifying plausible customers.
* Suggesting promising interactions or collaborations that have not yet been identified within an organization. 
* In Bioinformatics, link prediction can be used to find interactions between proteins.

The following model can be extended or modified to cater to the needs of various other social networks like Twitter, Google+, Foursquare, etc.
## Knowledge Engineering Process

Discussed below are the four major Knowledge Engineering Tasks:

### Acquisition & Learning
##### Data: 
* Acquired from http://snap.stanford.edu/data/egonets-Facebook.html

* This dataset consists of 'circles' (or 'friends lists') from Facebook.

* This anonymized dataset includes node features (profiles), circles, and ego networks.

* The edges are **undirected** .

*  10 ego-networks, consisting of 193 circles and 4,039 users.

*  Features of various nodes are described in the following format:` [Type]:[Subtype]:attributeName` 

*  Following figure represents an example of the attributes and the procedure of feature array formation.

##### Domain Knowledge: 

Following insights are meaningful while building our model for Link Prediction:

* The idea is to assign the connection weight `score(x, y)`  to pairs of nodes `<x, y>` , based on the input graph.

* The approaches adopted so far can be classified into:
  * *Methods based on node neighborhoods*: A number of approaches are based on the idea that two nodes x and y are more likely to form a link in the future if their sets of neighbors Γ(x) and Γ(y) have large overlap. Example:
    * Common neighbors
    * Jaccard’s coefficient
    * Preferential attachment
  * *Methods based on the ensemble of all paths*: A number of methods refine the notion of
    shortest-path distance by implicitly considering the ensemble of all paths between two nodes.

* Since we had multiple features associated with each node in an ego network, we performed our experiment based on the **similarity of features between the two nodes**.

* Machine Learning models like Support Vector Machine could classify the set of nodes into two: (1) Connection, (2) No connection, Neural Networks and regression techniques can be used for the same.




##### Task: 

> Given an unweighted, undirected graph `G = ⟨V,E⟩`  representing the topological structure of a social network in which each edge `e = ⟨u,v⟩ ∈ E`  represents an interaction between u and v that took place at a particular time `t(e)` , the two task can be described as:
>
> * **To find the highly influencing/ central node set N.**
>
>
> * **For time T greater than t(e), we need to predict and output a list of edges not present at t(e).** 

### Representation:
##### Data: 

* In order to represent complex data structure of a graph with various features attached to each node, `python-igraph` has been used.
* `Dictionary Data Structure` is deployed to store the corresponding features of each node.

### Development and Explanation:
##### Approach:

* ***Measures for Centrality***  : As our part of analysis, we used the following 4 centrality measures:
  * `Degree of nodes` : 
    - Core idea: To find the nodes that have highest number of  immediate neighbors (degree)
    - Input: Graph and a node 
    - Output: Degree of nodes.
  * `Closeness Centrality` : 
    * Core idea: A central node is one that is close, on average, to other nodes.
    * Input: Graph and a node 
    * Output: value [0,1] after standardization (1 being highly central)
  * `Betweeness Centrality` :
    * Core Idea: A central actor is one that acts as a bridge, broker or gatekeeper.
    * Input: Graph and a node 
    * Output: value [0,1] after normalization (1 being highly central)
  * `Eigenvector centrality` :
    * Core Idea: A central actor is connected to other central actors.
    * Input: Graph
    * Output: value [0,1] 
* ***Link Prediction***: Based on our survey[1], usability criteria and experiments, we have used the following Machine learning approach:
  * `Support Vector Machine` classification algorithm:
    * Core Idea: Segregating the two classes with a hyper-plane.
      * Here, two classes are: Linked and unlinked
    * Input:
      * Graph Dataset (separately for each ego network), with labels attached
      * Features (~230) dictionary
    * Output: Predicted association between two nodes `[x,y]` :
      * 0 if no association
      * 1 otherwise.
    * We divide out dataset in the ratio of **2:1:1**  for **Train:Validation:Test** 



##### Python Libraries used:

* `Plotly` : Graphing library for making interactive, publication-quality graphs online. 
* `IGraph` : igraph is a collection of network analysis tools with the emphasis on efficiency**, **portability and ease of use. igraph is open source and free. 
* `Numpy` :  Adds support for large, multi-dimensional arrays and matrices along with a large collection of high level mathematical functions to operate on these arrays. (dependency- Scikit)
* `Scipy` :  An open source Python library used for scientific computing and technical computing.(dependency- Scikit)
* `Scikit- Learn` : Simple and efficient tool for data mining and data analysis. Used for dimensionality reduction and implementing machine learning algorithms.

### Validation: Performance Evaluation:
##### Evaluation Interpretation: 

| Criteria        | Formula                                  | Score | Interpretation                           |
| --------------- | ---------------------------------------- | ----- | ---------------------------------------- |
| Accuracy        | ![{\mathit  {ACC}}=({\mathit  {TP}}+{\mathit  {TN}})/(P+N)](https://wikimedia.org/api/rest_v1/media/math/render/svg/31f7e08f6490e7182038c4ce27b87c483d6c3b4a) | 70%   | The results predicted were correct 70% of the time. |
| Precision Score | ![{\mathit {PPV}}={\mathit {TP}}/({\mathit {TP}}+{\mathit {FP}})](https://wikimedia.org/api/rest_v1/media/math/render/svg/699fcdb880b7f6a92742bc0845b8b60b59806a98) | 68%   | The links (1) predicted were correct 68% of the time. |
| F1 Score        | ![{\mathit {F1}}=2{\mathit {TP}}/(2{\mathit {TP}}+{\mathit {FP}}+{\mathit {FN}})](https://wikimedia.org/api/rest_v1/media/math/render/svg/8b64097b6362d28387a0c4650f2fed2bc5ea9fe9) | 65%   | It considers both precision and recall the of the test to compute the score |


## Replicating the results

In order to run the code provided in `SocialNetworkAnalysis.zip`

* Unzip the file

* Setting up the environment for execution:

  * Python version 2.7 or above.
  * Install the python libraries as described in the previous section.

* Setting up the dataset:

  ```
  python2.7 GenerateOtherDatasets.py
  ```

* To get the centrality measures and visualize the network:

  ```python
  python2.7 Centrality.py
  ```

* For Link Prediction and Evaluation:

  ```
  python2.7 Link_Prediction.py
  ```

  ​

------

[1]"Link prediction in multiplex online social networks" by Mahdi Jalili et al
