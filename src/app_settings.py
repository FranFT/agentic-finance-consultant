import os
from dotenv import load_dotenv
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=None)
    environment: str
    google_api_key: SecretStr
    google_gemini_model_name: str

    def __init__(self, env_file: str = '.env', **kwargs):
        # Load environment variables before pydantic.
        load_dotenv(env_file)
        super().__init__(**kwargs)