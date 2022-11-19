import numpy as np
import pandas as pd
import copy

class Node():
    id = 0
    def __init__(self, lu_over_time) -> None:
        self.id = Node.id
        Node.id += 1
        self.lu_over_time = np.array(lu_over_time)
        self.immediate_neighbors = set()
        
    def similarity(self, other):
        return np.mean(self.lu_over_time == other.lu_over_time)
    
    def __repr__(self):
        return f"Node({self.lu_over_time})"
    
    def __str__(self):
        return self.__repr__()
    
    def from_df(dataframe):
        nodes = {}
        for index, row in df.iterrows():
            nodes[index] = Node(row)
        return nodes
        
    def compute_similarity_matrix(nodes_dict):
        l = len(nodes_dict)
        similarity_matrix = np.zeros((l,l))
        for each in nodes_dict:
            for other in nodes_dict:
                similarity_matrix[each,other] = nodes_dict[each].similarity(nodes_dict[other])
        return similarity_matrix
    
    def invalidate(similarity_matrix, threshold):
        filled_similarity_matrix = copy.deepcopy(similarity_matrix)
        filled_similarity_matrix[filled_similarity_matrix<threshold] = np.nan
        
        return  filled_similarity_matrix
    
    def get_immediate_neighbor(self, neighborhood_info):
        return set(np.where(neighborhood[self.id]==1)[0])
    
    def get_neighborhood_map(nodes, neighborhood_info):
        neighborhood_map = {}
        for each in range(len(neighborhood_info)):
            neighborhood_map[each] = nodes[each].get_immediate_neighbor(neighborhood_info)
        return neighborhood_map
    
df = pd.DataFrame({"first":[1,1,1,1,1], "second": [1,1,2,1,1], "third": [1,1,2,2,1], "fourth":[1,2,1,1,2], "fifth": [1,1,2,1,2]})
df

nodes_dict = Node.from_df(df)
nodes_dict

mat = Node.compute_similarity_matrix(nodes_dict)

Node.invalidate(mat, 0.3)

neighborhood = np.array([[1,1,1,1,0],[1,1,0,1,1],[1,0,1,1,0],[1,1,1,1,1],[0,1,0,1,1]])
neighborhood

Node.get_neighborhood_map(nodes_dict, neighborhood)
