from util import Stack


def earliest_ancestor(ancestors, starting_node):
    pass


# UPER
# Understand
# A graph of relationship between parents and children
# data is formatted as a list of (parent, child) pairs
# each child is assigned a unique integer identifier

# Write a function that takes in a dataset of all individuals
# and the ID of an individual in the dataset
# and returns the earliest known ancestor (the farthest distance)
# from the individual
# If there is more than one ancestor tied for the result
# return the one with the lowest numeric ID
# If the individual has no parents, the function should return -1

"""
## How to solve (almost) any graph problem

1. Translate the problem in to graph terminology
    - Find what parts of the problem can be modeled as nodes / vertices
    - Find the part of the problem that can be modeled as Edges or Connections
2. Build Your Graph
    - use data from the problem to create a graph based on the way you have chosen to model it's component parts
3. Traverse your Graph
    - think about how you have decided to model your problems solution. look for key words or ideas that could point you toward a specific traversal algorithm.
    - look for keywords such as `shortest`, `fastest` or anything that could give you a clue as to what might be a good fit for the problem at hand
"""

# Put together a graph that adds vertices
# nodes are individual IDs
# edges are links between each ancestors
# Sample Graph/dataset/ancestors = [(10, 3), (4, 2), (1, 5), (7, 2)]

# Writing a DFS
# Initial a stack
# Initialize an empty set
# add the starting node to the stack
# while the stack isn't empty
# pop the path to the last item from the stack
# remove the last item from the path
# keep track of the visited items
# check if the removed last item has been visited
# if it hasn't

# Get neighbors of a given vertex by iD
# Performs a DFS to get the farthest ancestor and return the ID

if __name__ == '__main__':
    ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                 (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    ea = earliest_ancestor(ancestors, 1)
    print('ea', ea)
