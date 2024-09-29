def story_prompt(protagonist: str, others: str, language: str):
    return f"""
        __ASK__
        Generate a bedtime story for kids with {protagonist} as protagonist and {others}.
        Also extract a list of sentences, from 5 to 10, to use for illustrations
        
        __CONSTRAINTS__
        - The Story should be around 700 words long.
        - The ending should be satisfying and leave the main character in a happy place
        - Many bedtime stories end with a main character hugging a caregiver. This is a great way to send a child off to sleep
        - You want to engage the child and capture their imagination, but you don’t want them to have to expend too much brain power following the story. It’s a tricky skill to create vivid stories with simple language, but with practice you will be able to achieve this
        - Many classic bedtime stories end with the main character learning a valuable lesson or moral. Try to incorporate this into your tale as well, but write it in a way that is organic, not preachy
        - language must be {language}
        """
