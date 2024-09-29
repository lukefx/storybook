from storybook.story_generator import generate_story_with_images


def get_non_empty_input(text: str):
    user_input = input(text)
    while not user_input.strip():
        print("Input cannot be empty. Please try again.")
        user_input = input(text)
    return user_input


def main():
    print("*** Storybook creator")
    protagonist = get_non_empty_input("Who should the Protagonist be? ")
    others = get_non_empty_input("Cool, and give me some info on the plot: ")
    language = get_non_empty_input(
        "In which language should I create the story? ex. Italian "
    )
    generate_story_with_images(protagonist, others, language)


if __name__ == "__main__":
    main()
