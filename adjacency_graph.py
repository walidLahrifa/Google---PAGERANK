# Creation Data    :    07/11/2020
# Last Modification:    10/11/2020
# Authors          :    'LAHRIFA Walid' & 'EN NIARI SAAD'
# Short Description:    Programming Directed Graph Adjacency List representation in Python


import numpy as np


class Edge:
    """
  Class to represent a edge object
    """

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest


# :
class Graph:
    """
  Class to represent a graph object using Adjacency List representation
    """
    # Constructor
    def __init__(self, N, edges):

        # allocate memory for the adjacency list
        self.nodes = [j for j in range(N)]
        self.edges = edges
        self.adj = [[] for _ in range(N)]
        self.in_edges = [[] for _ in range(N)]

        # add edges
        for current in self.edges:
            # allocate node in adjacency List from src to dest
            self.adj[current.src].append(current.dest)

        for in_current in self.edges:
            # allocate node in adjacency List from dest to src
            self.in_edges[in_current.dest].append(in_current.src)


def printGraph(graph):
    """
  Print adjacency list representation of graph
    Parameters
    ----------
    Graph

    Returns
    -------
    Displayed Graph

    """
    for src in range(len(graph.adj)):
        # print current vertex and all its neighboring vertices
        print(f"{src} -> {graph.adj[src]} ", end="")
        print()
