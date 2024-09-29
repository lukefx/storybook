import glob
import io
import os
import re

from PIL import Image
from tqdm import tqdm

from storybook.entity.Book import Book
from storybook.image_generation.remote import generate_image
from storybook.llm.llm_story_generator import generate_story
from storybook.prompts.prompts import story_prompt


def slugify(string):
    string = string.lower()
    string = re.sub(r"[^a-z0-9\s\-_]", "", string)
    string = re.sub(r"\s+", "-", string)
    string = string.strip("-")
    return string


def create_story_folder(book_title):
    """Creates a folder for the story if it doesn't exist."""
    story_path = os.path.join("output", slugify(book_title))
    os.makedirs(story_path, exist_ok=True)
    return story_path


def save_image(illustration, story_path, index):
    """Generates and saves the image."""
    try:
        response_image = generate_image(illustration)
        image = Image.open(io.BytesIO(response_image))
        image.save(f"{story_path}/image_{index}.png")
    except Exception as e:
        print(f"{e} - Unable to generate image, skipping...")


def write_story_with_images(story, story_path, image_files):
    """Writes the story and appends images after every three sentences."""
    sentences = [
        sentence.strip() for sentence in story.split(".") if sentence.strip()
    ]  # Clean sentences
    image_count = len(image_files)

    with open(os.path.join(story_path, "story.md"), "w") as f:
        for i, sentence in enumerate(sentences):
            f.write(sentence + ".\n\n")
            if (i + 1) % 3 == 0 and (
                i // 3
            ) < image_count:  # Add image after every 3rd sentence
                f.write(f"![Image](image_{i // 3}.png)\n\n")

        # Append any remaining images that haven't been added
        for extra_image in range(i // 3 + 1, image_count):
            f.write(f"![Image](image_{extra_image}.png)\n")


def generate_story_with_images(protagonist, others, language):
    """Main function to generate the story and save it with images."""
    prompt = story_prompt(protagonist, others, language)
    book: Book = generate_story(prompt)

    print("Generating story...")
    # Create story folder
    story_path = create_story_folder(book.title)

    # Create illustrations
    for i, illustration in tqdm(
        enumerate(book.illustrations), desc="Generating images..."
    ):
        save_image(illustration, story_path, i)

    # Retrieve all generated image files
    image_files = sorted(glob.glob(os.path.join(story_path, "*.png")))

    # Write the story with images
    write_story_with_images(book.story, story_path, image_files)
