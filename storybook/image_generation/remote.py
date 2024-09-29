import requests

from storybook.config import get_app_config

config = get_app_config()


def generate_image(prompt: str) -> bytes:
    payload = {"inputs": f"cartoon style {prompt}"}
    headers = {"Authorization": f"Bearer {config.hf_api_key}"}
    response = requests.post(config.hf_model_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.content
