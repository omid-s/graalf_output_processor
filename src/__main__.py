"""
the main file for the GrAALF converter

"""

import json
import numpy as np
import networkx as nx
import os


def save_files(edge_ones: list, graphs: list, output_dir: str, edges: dict):
    """
    saves the sub graphs to the file
    :param edge_ones:
    :param graphs:
    :param output_dir:
    :param edges:
    :return:
    """
    data = []
    for pick in graphs:
        pick_edges = []
        for x in pick.nodes:
            for edge in edge_ones:
                if edge[0] == x or edge[1] == x:
                    pick_edges.append(edge[2])

        data.append(list(set(pick_edges)))

    cntr = 0

    # create the output directory if not exists
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for pick in data:
        cntr += 1
        with open(os.path.join(output_dir, "%d.json" % cntr), "w") as the_file:
            json.dump([edges[x] for x in pick], the_file)


def main(args):

    rows = []

    # read in the input file
    with open(args.input_name) as the_file:
        rows = json.load(the_file)

    # create nodes and edges
    nodes = []
    edges = {}
    edge_ones = []
    for x in rows:
        edges[x['sequence_number']] = x
        from_node = "%s-%s" % (x["from_id"], x["from_name"])
        to_node = "%s-%s" % (x["to_id"], x["to_name"])
        nodes.append(from_node)
        nodes.append(to_node)
        edge_ones.append((from_node, to_node, x['sequence_number']))

    if args.path_based:
        the_g = nx.MultiDiGraph()
    else:
        the_g = nx.Graph()

    the_g.add_nodes_from(nodes)
    for pick in edge_ones:
        the_g.add_edge(pick[0], pick[1], number=pick[2])

    if not args.path_based:
        S = [the_g.subgraph(c).copy() for c in nx.connected_components(the_g)]
    else:
        endnodes = []
        for pick in the_g.nodes:
            if the_g.in_degree(pick) > 0 and the_g.out_degree(pick) == 0:
                endnodes.append(pick)
        pathes = {x: [] for x in endnodes}

        for node in the_g.nodes:
            for dest in endnodes:
                if nx.has_path(the_g, node, dest):
                    pathes[dest].append(node)

        S = [the_g.subgraph(x).copy() for x in pathes]

    save_files(edge_ones=edge_ones, graphs=S,
               output_dir=args.output_dir, edges=edges)
