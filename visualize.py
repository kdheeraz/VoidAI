import networkx as nx
import matplotlib.pyplot as plt

plt.ion()

def visualize_memory_graph(memory_graph):
    """
    Visualizes a memory graph using NetworkX and Matplotlib.
    This function creates a directed graph from the provided memory_graph object,
    where each node represents a memory with associated labels and mood (calculated
    as the sum of affect values). Nodes are labeled with their labels and mood.
    Edges represent links between memories. The graph is displayed using a spring
    layout.
    Args:
        memory_graph: An object with a 'nodes' attribute (dict-like), where each node
            has 'labels' (dict), 'affect' (dict), and 'links' (iterable of node IDs).
    Returns:
        None. Displays the memory graph visualization interactively.
    """
    G = nx.DiGraph()
    for node_id, node in memory_graph.nodes.items():
        mood = round(sum(node.affect.values()), 2)
        label = f"{list(node.labels.values())}\nMood:{mood}"
        G.add_node(node_id, label=label)

        for linked_id in node.links:
            G.add_edge(node_id, linked_id)

    pos = nx.spring_layout(G, seed=42)
    plt.clf()
    nx.draw(G, pos, with_labels=False, node_size=800, node_color='skyblue')
    labels = nx.get_node_attributes(G, 'label')
    nx.draw_networkx_labels(G, pos, labels)
    plt.title("🧠 AGI Memory Stream (Dependent Origination)")
    plt.pause(0.1)
