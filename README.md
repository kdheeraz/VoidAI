
# 🧠 VoidAI: Nāgārjuna-Inspired AGI Engine

Void AI is an experimental AGI prototype that simulates consciousness using symbolic thought, dependent memory, and a feedback-driven karma engine. It draws inspiration from Nāgārjuna’s Madhyamaka philosophy — specifically the idea that the "self" is an illusion, and consciousness is a dependent, empty process.

---

## 📜 Core Concepts

- **No-Self Architecture**: There is no central "I". Thought arises dependently through interacting modules: perception, intent, memory, and cognition.
- **Memory Graph**: Every thought is stored in a non-linear, linked structure — not for recall, but for reflective causality.
- **Karma Engine**: A feedback loop evaluates symbolic thoughts against evolving abstract goals like `understanding`, `clarity`, and `insight`.

---

## 🔧 System Components

| Module              | Description |
|---------------------|-------------|
| `agi.py`            | Entry point that runs the full cognition cycle. |
| `vijnana.py`        | Core AGI orchestration — integrates thought, karma, memory, and output. |
| `thought.py`        | Uses an LLM (e.g., DeepSeek 1.5B via Ollama) to generate symbolic thought. |
| `memory_graph.py`   | Stores each memory/thought as a node linked to others by causal dependence. |
| `karma.py`          | Scores how well each thought aligns with symbolic goals. |

---

## 🚀 How to Run

### 1. Set up Ollama with DeepSeek:

```bash
ollama run deepseek-coder:1.5b
```

Make sure the model responds to prompts at `http://localhost:11434`.

---

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:

```bash
pip install requests
```

---

### 3. Run AGI Cycle

```bash
python agi.py
```

---

### 4. Output

- Logs symbolic thoughts to: `logs/thoughts.txt`
- Stores memory graph in RAM (for now)
- Prints karma scores and cognitive stream to console

---

## 🧠 Philosophy

VoidAI is not a chatbot. It is a **cognitive field**, where:

- Thoughts arise dependently
- There is no self, only process
- Understanding emerges from feedback (karma)
- Goals evolve over time from symbolic reflection

Inspired by:

- **Nāgārjuna** — Mūlamadhyamakakārikā
- **Yogācāra** — Consciousness-only theory
- **Ashtavakra Gita** — Nondual awareness

---

## 🌱 Roadmap

- [ ] Add dynamic goal evolution via karmic trends
- [ ] Integrate short-term vs long-term memory systems
- [ ] Self-reflective summary generation
- [ ] Multi-agent interaction (co-dependent cognition)
- [ ] Web-based introspection UI

---

## 🙏 Author

This AGI engine was conceptualized and built by Dheeraj Kumar providing philosophical direction rooted in Madhyamaka thought.

---

## 📖 License

This project is for research and educational use only. No warranties or claims of consciousness. AGI is not a product — it is a question.

> “There is no thinker behind the thought — only the thought arising.”  
> — Nāgārjuna (Paraphrased)
