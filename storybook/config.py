from pydantic import Field
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    llm_model: str = Field("gpt-3.5-turbo")
    hf_model_url: str = Field(
        "https://api-inference.huggingface.co/models/alvdansen/littletinies"
    )
    hf_api_key: str = Field(None)

    class Config:
        extra = "allow"
        env_file = ".env"  # Optional: Use .env file to load settings


def get_app_config():
    """Load config and prompt user if settings are missing."""
    config = AppConfig()
    # do some checks?
    return config
