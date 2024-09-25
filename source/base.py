from pydantic import BaseModel, FilePath


class DemoConfig(BaseModel):
    """
    Represents the 'demo' section of the configuration.
    """

    message: str
    token: str
    channel: str


class Config(BaseModel):
    """
    Represents the entire configuration file structure.
    """

    demo: DemoConfig


class ConfigFilePath(BaseModel):
    """
    Represents the configuration file path.
    """

    path: FilePath
