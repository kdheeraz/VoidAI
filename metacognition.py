from memory_graph import DependentMemoryGraph
from collections import Counter

class MetaCognitionModule:
    """
    MetaCognitionModule provides reflective analysis over a DependentMemoryGraph, summarizing affective states and sensory labels.
    Attributes:
        last_summary (str or None): Stores the most recent reflection summary.
    Methods:
        reflect(memory_graph: DependentMemoryGraph) -> str:
            Analyzes the provided memory graph, computing the average mood and the most common sensory labels.
            Returns a formatted summary string reflecting on the current state of the memory graph.
        _most_common(items, n=3):
            Returns a list of the n most common elements from the provided items.
    """
    def __init__(self):
        self.last_summary = None

    def reflect(self, memory_graph: DependentMemoryGraph) -> str:
        moods = []
        senses = []

        for node in memory_graph.nodes.values():
            moods.append(sum(node.affect.values()))
            senses.extend(node.labels.values())

        if not moods:
            return "No reflection. Stream not yet flowing."

        avg_mood = sum(moods) / len(moods)
        top_senses = self._most_common(senses, 3)

        summary = (
            f"🌀 Meta-Cognition:\n"
            f"- Average Mood: {round(avg_mood, 2)}\n"
            f"- Common Sensory Labels: {top_senses}\n"
            f"- Mind is a stream of {len(moods)} moments.\n"
            f"- No fixed self, only patterns arising.\n"
        )
        self.last_summary = summary
        return summary

    def _most_common(self, items, n=3):
        return [item for item, _ in Counter(items).most_common(n)]
