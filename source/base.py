"""
Definition of the config structure

"""

from pydantic import BaseModel, FilePath


class TwitchConfig(BaseModel):
    """
    Represents the 'demo' section of the configuration.
    """

    token: str
    channel: str
    prefix: str


class AiConfig(BaseModel):
    """
    Represents the 'ai' section of the configuration.
    """

    base_url: str
    api_key: str
    model: str
    temperature: float
    personality: str


class Config(BaseModel):
    """
    Represents the entire configuration file structure.
    """

    twitch: TwitchConfig
    ai: AiConfig


class ConfigFilePath(BaseModel):
    """
    Represents the configuration file path.
    """

    path: FilePath
