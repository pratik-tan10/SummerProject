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
            new_node = Node(row)
            nodes[new_node.id] = new_node
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
        neighbors = set(np.where(neighborhood_info[self.id]==1)[0])
        for each in list(neighbors):
            if each == self.id:
                neighbors.remove(each)
        return neighbors
    
    def get_neighborhood_map(nodes, neighborhood_info):
        neighborhood_map = {}
        for each in range(len(neighborhood_info)):
            neighborhood_map[each] = nodes[each].get_immediate_neighbor(neighborhood_info)
        return neighborhood_map
    
    def make_pair(self, neighborhood_info):
        pairs = set()
        for each in self.get_immediate_neighbor(neighborhood_info):
            pairs.add((self.id, each))
        return pairs
    def reset_counter():
        Node.id = 0

df = pd.DataFrame({"first":[1,1,1,1,1], "second": [1,1,2,1,1], "third": [1,1,2,2,1], "fourth":[1,2,1,1,2], "fifth": [1,1,2,1,2]})
df

nodes_dict = Node.from_df(df)
nodes_dict

mat = Node.compute_similarity_matrix(nodes_dict)
mat

Node.invalidate(mat, 0.3)

neighborhood = np.array([[1,1,1,1,0],[1,1,0,1,1],[1,0,1,1,0],[1,1,1,1,1],[0,1,0,1,1]])
neighborhood

Node.get_neighborhood_map(nodes_dict, neighborhood)


a = [nodes_dict[i].make_pair(neighborhood) for i in nodes_dict]

a

class Clusterer():
    Clusters = {}
    counter = 0
    def __init__(self, nodes_dict, neighborhood):
        self.nodes_dict = nodes_dict
        self.neighborhood = neighborhood
        self.S = set()
        self.P = set()
        self.R = set()
        self.C = set()
        self.possible_choices = set(list(self.nodes_dict))
        self.similarity_matrix = Node.compute_similarity_matrix(nodes_dict)
    
    def is_inset(self, testnode):
        for cluster in Clusters.values():
            for eachnode in cluster:
                if testnode.id == eachnode.id:
                    return True
        return False
    
    def choose_node(self):
        selected_node = self.nodes_dict[np.random.choice(list(self.possible_choices))]
        self.possible_choices.remove(selected_node.id)
        return selected_node      
        
    def clean_pairs(self,node):
        self.P = node.make_pairs(self.neighborhood)
        for each in list(p):
            if each in self.R:
                self.P.remove(each)
            if each[0] in self.S and each[1] in self.S:
                self.P.remove(each)
            
            if self.similarity_matrix[each[0], each[1]] < self.threshold:
                self.R.add(each)
        
    def run_clustering(self):
        selected_node = self.choose_node()
        
        self.clean_pairs(selected_node)
        cleans = list(self.P)
        if len(cleans)>0:
            maxsimilarity = 0
            for each in cleans:
                similarity = self.similarity_matrix[each[0], each[1]]
                if similarity > maxsimilarity:
                    maxsimilarity = similarity
                    new_node = each[1]
            self.S.add(new_node)

