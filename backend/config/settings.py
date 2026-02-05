from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, computed_field
from typing import Optional
from urllib.parse import quote_plus

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    Uses Pydantic BaseSettings for automatic .env file loading and validation.
    """


settings = Settings()
