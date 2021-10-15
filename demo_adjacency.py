# Creation Data    :    10/11/2020
# Last Modification:    10/11/2020
# Authors          :    'LAHRIFA Walid' & 'EN NIARI SAAD'
# Short Description:    Demo Adjacency Graph


from datetime import timedelta
from timeit import default_timer as timer
from adjacency_graph import Edge, Graph, printGraph
from pagerank import pagerank

# First Graph
edges1 = [Edge(0, 1), Edge(1, 0), Edge(1, 2), Edge(2, 3), Edge(3, 0)]
graph1 = Graph(4, edges1)

# Second Graph
edges2 = [Edge(0, 1), Edge(1, 0), Edge(1, 2), Edge(2, 0)]
graph2 = Graph(3, edges2)

# Third Graph
edges3 = [Edge(0, 1), Edge(1, 0), Edge(1, 2), Edge(2, 1), Edge(2, 3), Edge(3, 4), Edge(4, 3), Edge(4, 0)]
graph3 = Graph(5, edges3)

# Fourth Graph
edges4 = [Edge(0, 1), Edge(1, 0), Edge(1, 2), Edge(2, 1), Edge(0, 2), Edge(2, 0)]
graph4 = Graph(3, edges4)

# list of demo graph
lst_graph = [graph1, graph2, graph3, graph4]


def diplay_graph(graph, zap_factor, graph_name):
    print("****************************   Graph Information: " + str(graph_name) + "   ****************************")
    zap_factor = 0.15
    printGraph(graph)
    print("Node  Number     : ", len(graph.nodes))
    print("Edges Number     : ", len(graph.edges))

    print("************** Ranks Calculation ****************")
    print("ZAP Factor      : ", zap_factor)
    start_calc = timer()
    ranks = pagerank(graph, zap_factor)
    end_calc = timer()
    calc_time = timedelta(seconds=end_calc - start_calc)
    print("Updated Ranks   : ", ranks)
    print("Calculation Time: ", str(calc_time) + " Seconds\n")


i = 1
for graph in lst_graph:
    diplay_graph(graph, 0.15, i)
    i += 1
