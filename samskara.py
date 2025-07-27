from memory_graph import DependentMemoryGraph

class SamskaraModule:
    """
    SamskaraModule manages a memory graph of affective states and forms behavioral intents based on affect analysis.
    Attributes:
        memory_graph (DependentMemoryGraph): The underlying graph structure storing affective memory nodes.
    Methods:
        update_memory(labels, affect):
            Adds a new node to the memory graph with the given labels and affective state.
        form_intent() -> str:
            Analyzes the latest affective state and similar past states to determine an intent.
            Returns:
                str: One of "Engage", "Withdraw", or "Contemplate" based on the computed mood.
    """
    def __init__(self):
        self.memory_graph = DependentMemoryGraph()

    def update_memory(self, labels, affect):
        self.memory_graph.add_node(labels, affect)

    def form_intent(self) -> str:
        latest = self.memory_graph.nodes[self.memory_graph.last_node_id]
        latest_affect = latest.affect
        similar = self.memory_graph.find_similar_node(latest_affect)

        mood = sum(latest_affect.values())
        if similar:
            past_mood = sum(similar.affect.values())
            mood = (mood + past_mood) / 2

        if mood > 0.3:
            return "Engage"
        elif mood < -0.3:
            return "Withdraw"
        else:
            return "Contemplate"
