import os
cwd = os.getcwd()
print(cwd)
import sys
sys.path.append('/home/shawasar/.local/lib/python3.5/site-packages')
import numpy
from random import choice
import pandas as pd
import statistics
import networkx as nx
import argparse
import os.path

def pick_random(number, graph, random_nodes, possible_nodes):
    """
    This recursive function will return a list of randomly selected nodes in the network
    The length of the list returned will be the number provided as an argument
    Arguments:
     - take a number, to specify how many nodes you want
     - a graph (network)
     - the nodes you have so far (starts as []) (for recursion)
     - all nodes you want to randomly select from, if it is the entire graph use set(graph.nodes)
    example:
    test = pick_random(10, G, [], set(G.nodes()))    
    
    """
    if number == 0: #base case
        return random_nodes
    else:
        found = choice(list(graph.nodes()))
        neighbors = [found]  
        possible_nodes.difference_update(neighbors) #so that we don't select the same node twice
        random_nodes.append(found)
        pick_random(number-1, graph, random_nodes, possible_nodes )
    return random_nodes


def sum_total_shortest_path(nodes, G):
    """
    This function will return the sum of the shortest paths between each two nodes in the list
    Arguments:
     - take a list of node names
     -a graph
    example using the output of previous function:
    sum_total_shortest_path(test, G)
    
    """
    
    sum_path = 0
    path_all = []
    for node in range(len(nodes)-1):
        for node2 in range(node+1, len(nodes)):
            if nodes[node] in G and nodes[node2] in G:
                if nx.shortest_path(G, nodes[node], nodes[node2]) != None:
                    sp = nx.shortest_path(G,nodes[node],nodes[node2])
                    sum_path += len(sp)
                    path_all.append(sp)
            else:
                print("NOT FOUND")
    return(sum_path)

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file does not exist")
    else:
        print("file is valid ")
        return open(arg, 'r')  # return an open file handle

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("network", help="network file in gml format", metavar="Network")
    parser.add_argument("nodes_file", help="list of nodes in text file")
    parser.add_argument("num_iterations", help="number of iterations")
    parser.add_argument("-c", "--connected", help="check if network is fully connected", action="store_true")
    parser.add_argument("-f", dest="filename",
                    help="random nodes taken from this file rather than the entire network", metavar="FILE", type=lambda x: is_valid_file(parser, x))
    args = parser.parse_args()
    
    if args.connected:
        print("connectivity turned on")
        H = nx.read_gml(args.network)
        if nx.is_connected(H):
            print("network is fully connected")
    else:
        H = nx.read_gml(args.network)
        
    if args.filename:
        print("file supplied")
        with open(args.filename) as f:
            subgraph_nodes = f.read().splitlines()
        found_subgraph_nodes = [] 
        for node in subgraph_nodes:
            if node in H:
                found_subgraph_nodes.append(node)     
        print("subgraph nodes number is  " + str(len(subgraph_nodes)))
        H = H.subgraph(found_subgraph_nodes)
        if not nx.is_connected(H):
            print("subgraph not fully connected")
        #print(pick_random(4, H, [], set(H.nodes())))
        
    print('sys.argv is', sys.argv)
    #script = sys.argv[0] #script name
    #network = sys.argv[1] #first arg, the network chlamyNET.gml
    #nodes_file = sys.argv[2]#second arg, list of nodes 
    #num_iterations = int(sys.argv[3]) #number of times you want to randomly take the same number of nodes 
    
    with open(args.nodes_file) as f:
        mutated_nodes = f.read().splitlines()
    
    print("first node in list " + str(mutated_nodes[0]))
    print("length of all mutated nodes " + str(len(mutated_nodes)))
    
    print("name of network file " + str(args.network))
 
    nodes_found = []
    not_found = 0 
    ma_genes = []
    for gene in mutated_nodes:
        if gene not in H:
            not_found += 1
        else:
            ma_genes.append(gene)
    num_nodes = len(ma_genes)
    print("nodes found in the network  "+ str(num_nodes))
    print("nodes NOT found in network " + str(not_found))
    
    mutated_nodes_distance = sum_total_shortest_path(ma_genes, H)
    print("shortest path for mutated nodes  " + str(mutated_nodes_distance))
    
   
    random_selections = []
    for i in range(int(args.num_iterations)):
        print("i is " + str(i))
        random_nodes = (sum_total_shortest_path(pick_random(num_nodes, H, [], set(H.nodes())) , H))
        random_selections.append(random_nodes)
        print("shortest path for random nodes " + str(random_nodes))

    shorter_distance = 0 #num of randomly selected nodes that were more clustered than the mutated nodes
    total = 0
    for x in random_selections:
        if x < mutated_nodes_distance:
            shorter_distance += 1
        total += 1
    print("shorter found is  " + str(shorter_distance) + " out of total  " + str(total))

if __name__ == '__main__':
   main()