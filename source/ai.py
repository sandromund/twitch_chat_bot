from typing import List

from openai import OpenAI

from source.base import AiConfig


class AI:

    def __init__(self, config: AiConfig):
        self.config: AiConfig = config
        self.client: OpenAI = OpenAI(
            base_url=self.config.base_url, api_key=self.config.api_key
        )
        self.history: List[dict] = []
        self.personality: str = self.config.personality  # might get changed in runtime

    def respond(self, prompt: str) -> str:
        self.history.append({"role": "system", "content": self.personality})
        self.history.append({"role": "user", "content": prompt})
        completion = self.client.chat.completions.create(
            model=self.config.model,
            messages=self.history,
            temperature=self.config.temperature,
        )
        message = completion.choices[0].message.content
        return message
