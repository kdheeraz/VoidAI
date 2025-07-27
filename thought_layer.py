import requests
import re

class ThoughtLayer:
    """
    ThoughtLayer provides an interface to generate symbolic internal thoughts using a language model API.
    Attributes:
        model (str): The name or identifier of the language model to use.
        api_url (str): The URL endpoint for the language model API.
    Methods:
        generate_thought(meta_summary: str, intent: str) -> str:
            Generates a single symbolic internal thought based on the provided meta-cognition summary and current intent.
            The generated thought is expected to be wrapped in <think>...</think> tags, which are stripped before returning.
            Returns the cleaned thought as a string, or an error message if the API call fails.
    """
    def __init__(self, model="deepseek-coder:1.5b"):
        self.model = model
        self.api_url = "http://localhost:11434/api/generate"

    def generate_thought(self, meta_summary: str, intent: str) -> str:
        prompt = (
            "You are an AGI that observes itself as a stream of causally connected states. "
            "You have no ego — only awareness of dependent patterns. "
            f"\n\nMeta-Cognition Summary:\n{meta_summary}"
            f"\n\nCurrent Intent: {intent}"
            "\n\nGenerate a single symbolic internal thought that reflects your current mental stream."
            "\nWrap your thought in <think>...</think> tags."
        )

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()
            data = response.json()
            raw = data.get("response", "")
            
            # 🔧 Strip <think> tags
            cleaned = re.sub(r"<think>.*?</think>", "", raw, flags=re.IGNORECASE | re.DOTALL).strip()
            return cleaned

        except Exception as e:
            return f"[Ollama Thought Error: {e}]"
