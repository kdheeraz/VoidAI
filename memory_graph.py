import uuid
from collections import defaultdict
from typing import Dict, List, Optional

class MemoryNode:
    def __init__(self, labels: Dict[str, str], affect: Dict[str, float]):
        self.id = str(uuid.uuid4())
        self.labels = labels
        self.affect = affect
        self.links: List[str] = []

class DependentMemoryGraph:
    """
    A graph-based structure to manage and relate memory nodes with affective attributes.
    The DependentMemoryGraph class maintains a directed graph of MemoryNode instances,
    where each node can be linked to others, and nodes are compared based on their affective states.
    Attributes:
        nodes (Dict[str, MemoryNode]): A mapping from node IDs to MemoryNode instances.
        graph (Dict[str, List[str]]): Adjacency list representing directed edges between nodes.
        last_node_id (Optional[str]): The ID of the most recently added node.
    Methods:
        add_node(labels: Dict[str, str], affect: Dict[str, float]):
            Adds a new MemoryNode to the graph with the given labels and affect values.
            Automatically links the new node to the previously added node, if any.
        link_nodes(from_id: str, to_id: str):
            Creates a directed link from one node to another in the graph.
        find_similar_node(affect: Dict[str, float]) -> Optional[MemoryNode]:
            Finds and returns the node whose affect values are most similar to the given affect dictionary,
            using Euclidean distance as the similarity metric.
    """
    def __init__(self):
        self.nodes: Dict[str, MemoryNode] = {}
        self.graph: Dict[str, List[str]] = defaultdict(list)
        self.last_node_id: Optional[str] = None

    def add_node(self, labels: Dict[str, str], affect: Dict[str, float]):
        node = MemoryNode(labels, affect)
        self.nodes[node.id] = node

        if self.last_node_id:
            self.link_nodes(self.last_node_id, node.id)

        self.last_node_id = node.id

    def link_nodes(self, from_id: str, to_id: str):
        self.nodes[from_id].links.append(to_id)
        self.graph[from_id].append(to_id)

    def find_similar_node(self, affect: Dict[str, float]) -> Optional[MemoryNode]:
        def distance(a, b):
            return sum((a.get(k, 0) - b.get(k, 0))**2 for k in set(a) | set(b))

        if not self.nodes:
            return None
        return min(self.nodes.values(), key=lambda node: distance(node.affect, affect))
