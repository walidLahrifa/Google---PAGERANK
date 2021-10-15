# Creation Data    :    03/11/2020
# Last Modification:    04/11/2020
# Authors          :    'LAHRIFA Walid' & 'EN NIARI SAAD'
# Short Description:    Programming 'PageRank' Algorithm

# Function that calculate the degre of a given node
def degre(graph, node):
    """
    :param node:
    :return The outbound of the node:
    """
    return graph.degree(node)


# Function calculate the Page Rank of a given graph
def pagerankx(graph,zap_factor):
    """
    :param graph:
    :return Returns a dictionary where the keys are the node/page names and the values are
    the calculated pagerank score for that given node/page :
    """

    # n Represent the number of the graph nodes
    n = len(graph.nodes)

    # ZAP Factor: generally recommended between 0.1 & 0.2
    d = zap_factor

    # Init_val is the initial value for the coefficient of the PageRank for all pages
    init_val = 1.0 / n

    # Association of the initial values to all the nodes/pages

    ranks = dict(zip(graph.nodes, [init_val] * n))

    updated_ranks = ranks.copy()

    # Calculate new rank for each node
    for node in ranks.items():
        rank_sum = 0.0

        # Iterate through incoming nodes
        # R n+1 (p) = d/N + (1-d) * Sigma qp 1/degre(q) * Rn(q)
        for incoming_edge in graph.in_edges(node[0]):
            incoming_node = incoming_edge[0]
            rank_incoming_node = ranks[incoming_node]

            transfer_amount = (1-d) * rank_incoming_node / degre(graph, incoming_node)
            rank_sum = rank_sum + transfer_amount

        updated_ranks[node[0]] = d/n + rank_sum

    # Set ranks to the new ranks calculated in this iteration
    ranks = updated_ranks
    return ranks
