"""
This module defines an AI wrapper class for interacting with the OpenAI API.
It handles the configuration and interaction with a chat-based AI model.
"""

from typing import List

from openai import OpenAI

from source.base import AiConfig


# pylint: disable=R0903
class AI:
    """
    A class to interface with the OpenAI chat completion API.

    Attributes:
        config (AiConfig): Configuration object with OpenAI settings.
        client (OpenAI): The OpenAI client initialized with API key and base URL.
        history (List[dict]): Conversation history with AI, stored as a list of messages.
        personality (str): The AI's personality which can be updated during runtime.
    """

    def __init__(self, config: AiConfig):
        """
        Initializes the AI class with configuration settings.

        Args:
            config (AiConfig): The configuration object containing model,
            API key, and other settings.
        """
        self.config: AiConfig = config
        self.client: OpenAI = OpenAI(
            base_url=self.config.base_url, api_key=self.config.api_key
        )
        self.history: List[dict] = []
        self.personality: str = self.config.personality  # might get changed in runtime

    def respond(self, prompt: str) -> str:
        """
        Sends a prompt to the OpenAI chat model and returns the AI's response.

        Args:
            prompt (str): The user's input message.

        Returns:
            str: The AI's response based on the provided prompt and chat history.
        """
        self.history.append({"role": "system", "content": self.personality})
        self.history.append({"role": "user", "content": prompt})
        completion = self.client.chat.completions.create(
            model=self.config.model,
            messages=self.history,
            temperature=self.config.temperature,
        )
        message = completion.choices[0].message.content
        return message
