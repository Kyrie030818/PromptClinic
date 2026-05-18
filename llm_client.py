import os
import requests

class LLMClient:
    def __init__(self) -> None:
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
        self.model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
        
        if self.base_url:
            self.base_url = self.base_url.rstrip("/")

    def chat_with_history(self, messages: list) -> str:
        """Call DeepSeek API with a list of messages (conversation history)."""
        if not self.api_key:
            return "Error: DEEPSEEK_API_KEY is not configured. Please set it in the .env file."

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.25,
            "max_tokens": 6000,
        }

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=60,
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            return f"Error: API request failed. Network issue: {e}"
        except (KeyError, ValueError) as e:
            return f"Error: Failed to parse API response. Detail: {e}"