# Creation Data    :    03/11/2020
# Last Modification:    10/11/2020
# Authors          :    'LAHRIFA Walid' & 'EN NIARI SAAD'
# Short Description:    Graph - Generator using NetworksX library

"""
Graph - Generator using NetworksX library
"""
import matplotlib.pyplot as pl
import networkx as nx
from networkx.generators.random_graphs import erdos_renyi_graph
from pagerankx import pagerankx
from timeit import default_timer as timer
from datetime import timedelta

# Small Demo with four Edges
zap_factor_graph_demoI = 0.15
node_number_graph_demoI = 4
probability_creation_graph_demoI = 0

start_gen = timer()
graph_demoI = erdos_renyi_graph(n=node_number_graph_demoI, p=probability_creation_graph_demoI, seed=None, directed=True)
end_gen = timer()
gen_time_demoI = timedelta(seconds=end_gen - start_gen)

graph_demoI.add_edge(1, 0)
graph_demoI.add_edge(2, 0)
graph_demoI.add_edge(3, 0)

# Medium Demo with 1000 Edges
zap_factor_graph_demoII = 0.15
node_number_graph_demoII = 10
probability_creation_graph_demoII = 1

start_gen = timer()
graph_demoII = erdos_renyi_graph(n=node_number_graph_demoII, p=probability_creation_graph_demoII, seed=None,
                                 directed=True)
end_gen = timer()
gen_time_demoII = timedelta(seconds=end_gen - start_gen)


def calculate_rank_page(graph, zap_factor, gen_time):
    print("\n************** Graph Informations **************")
    print("Node  Number     : ", len(graph.nodes))
    print("Edges Number     : ", len(graph.edges))
    if (len(graph.nodes) < 100):
        print("Edges           : ", graph.edges)
    print("Generation Time : ", str(gen_time) + " Seconds")

    print("************** Ranks Calculation ****************")
    print("ZAP Factor      : ", zap_factor)
    start_calc = timer()
    ranks = pagerankx(graph, zap_factor)
    end_calc = timer()
    calc_time = timedelta(seconds=end_calc - start_calc)
    #print("Updated Ranks   : ", ranks)
    print("Calculation Time: ", str(calc_time) + " Seconds")
    print("************************************************")


def generate_graph(node_nbr, probability_creation):
    start = timer()
    graph = erdos_renyi_graph(n=node_nbr, p=probability_creation, seed=None,
                              directed=True)
    #nx.draw(graph)
    #pl.savefig("graph_"+str(node_nbr)+".png")

    end = timer()
    return graph, end - start


# calculate_rank_page(graph_demoII, zap_factor_graph_demoII, gen_time_demoII)

graph_time = generate_graph(node_nbr=100000, probability_creation=0.001)
calculate_rank_page(graph=graph_time[0], zap_factor=0.15, gen_time=graph_time[1])
