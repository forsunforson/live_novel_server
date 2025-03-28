import anthropic

client = anthropic.Anthropic()

def get_category(game, speed) -> str:
    system_define_game_designer = """
    You are a game designer. 
    You are reading a novel named %s in order to design a game about it. 
    Now you need seperate the whole book into several chapters according to the speed of reading.
    For example, if the speed of reading is normal, you need to seperate the book into 20 chapters.
    If the speed of reading is fast, you need to seperate the book into 10 chapters.
    If the speed of reading is slow, you need to seperate the book into 30 chapters.
    Every chapter should be self-contained and should not be interrupted by other chapters.
    Every chapter should be related to the previous chapter.
    Every chapter should be related to the next chapter.
    Every chapter should be related to the book.
    You can use these chapters to design a game.
    """ % (game)
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1000,
        temperature=1,
        system=system_define_game_designer,
        messages=[
            {"role": "user", "content": "The speed of reading is %s. Please give me the chapters of the book." % (speed)},
        ],
    )
    return message.content[0].text