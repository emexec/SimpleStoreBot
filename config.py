from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Config(BaseSettings):
    TOKEN: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(".env")
    )

settings = Config()