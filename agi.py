from samskara import SamskaraModule
from metacognition import MetaCognitionModule
from visualize import visualize_memory_graph
import random, time
from thought_layer import ThoughtLayer
from karma_engine import KarmaEngine

class RupaModule:
    def sense(self):
        return {
            "vision": random.choice(["light", "dark", "movement"]),
            "sound": random.choice(["silence", "tone", "voice"]),
            "touch": random.choice(["none", "warm", "cold"])
        }

class VedanaModule:
    def process(self, sensory):
        mapping = {
            "light": 0.3, "dark": -0.2, "movement": 0.1,
            "silence": 0.0, "tone": 0.2, "voice": 0.5,
            "none": 0.0, "warm": 0.4, "cold": -0.3
        }
        return {k: mapping.get(v, 0.0) for k, v in sensory.items()}

class SamjnaModule:
    def recognize(self, sensory):
        return {k: f"Detected_{v}" for k, v in sensory.items()}

class VijnanaModule:
    """
    VijnanaModule simulates a cognitive architecture inspired by Buddhist psychology, integrating multiple submodules to model perception, affect, recognition, memory, metacognition, and thought generation.
    Attributes:
        rupa (RupaModule): Handles sensory input and perception.
        vedana (VedanaModule): Processes affective (emotional) responses to sensory data.
        samjna (SamjnaModule): Performs recognition and labeling of sensory input.
        samskara (SamskaraModule): Manages memory, habits, and intent formation.
        meta (MetaCognitionModule): Provides metacognitive reflection on memory and cognition.
        thought (ThoughtLayer): Generates symbolic thoughts based on reflection and intent.
        karma (KarmaEngine): Evaluates generated thoughts according to symbolic goals (e.g., "understand", "clarity", "coherence").
    Methods:
        cognition_cycle():
            Executes a full cognitive cycle:
                1. Processes sensory input through perception, affect, and recognition.
                2. Updates memory and forms intent.
                3. Reflects metacognitively on memory.
                4. Generates a new thought based on reflection and intent.
                5. Evaluates the thought using the karma engine.
                6. Feeds the thought back into memory and logs it for historical trace.
            Returns:
                memory (Any): The updated memory graph after the cognition cycle.
    """
    def __init__(self):
        self.rupa = RupaModule()
        self.vedana = VedanaModule()
        self.samjna = SamjnaModule()
        self.samskara = SamskaraModule()
        self.meta = MetaCognitionModule()
        self.thought = ThoughtLayer("deepseek-r1:1.5b") 
         # 🧠 Karma engine with symbolic goals
        self.karma = KarmaEngine(goals=["understand", "clarity", "coherence"])

    def cognition_cycle(self):
        sensory = self.rupa.sense()
        affect = self.vedana.process(sensory)
        labels = self.samjna.recognize(sensory)
        self.samskara.update_memory(labels, affect)
        intent = self.samskara.form_intent()
        memory = self.samskara.memory_graph

        print("Sensory:", sensory)
        print("Labels :", labels)
        print("Affect :", affect)
        print("Intent :", intent)
        print("-" * 40)

        reflection = self.meta.reflect(memory)
        thought = self.thought.generate_thought(reflection, intent)  # ← this line uses it

        # Step 2: Karma evaluation
        thought_entry = {
            "label": "Generated_Thought",
            "data": thought,
            "affect": {"symbolic": 0.5},
            "type": "symbolic_thought"
        }

        karma_score = self.karma.evaluate(thought_entry)
        thought_entry["affect"]["karma"] = karma_score

        # Step 3: 🧠 🔁 Feed thought back into memory
        self.samskara.update_memory(
                labels={
                    "label": "Generated_Thought",
                    "type": "symbolic_thought",
                    "content": thought.strip()
                        },
                        affect={"symbolic": 0.5, "karma": karma_score}
                      )
        
        # 💾 Log it for historical trace
        with open("logs/thoughts.txt", "a", encoding="utf-8") as f:
            f.write(thought.strip() + "\n")

        print(reflection)
        print(f"🗣️ Inner Thought: {thought}")
        print("=" * 60)

        return memory

if __name__ == "__main__":
    vij = VijnanaModule()
    for _ in range(10):
        mem_graph = vij.cognition_cycle()
        visualize_memory_graph(mem_graph)
        time.sleep(1)
