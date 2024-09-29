import instructor
from litellm import completion

from storybook.config import get_app_config
from storybook.entity.Book import Book


def generate_story(prompt: str) -> Book:
    client = instructor.from_litellm(completion)
    llm_response: Book = client.chat.completions.create(
        model=get_app_config().llm_model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        response_model=Book,
    )

    return llm_response
