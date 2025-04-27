from custom_types.struct import PlayRequest, Message

from client.anthropic import claude_text_generator
from context.context_builder import build_context
from storage.file_storage import dump_2_file

system_define_game_master = """Game Rules:
Let's play a text-based game of %s. I will play one of the characters, and you will narrate the storyline and play the other characters, guiding me through the plot framework. After each interaction or dialogue, we will move to the next part of the story.
In your responses, please pay attention to the following points:

Summarize the key plot points of the script and identify critical interaction nodes.
Before reaching an interaction event, you can recite the script content verbatim to ensure the original text's value, using the original descriptions and dialogues as much as possible.
Upon reaching an interaction node, you will provide interaction options from the character's perspective or as a narrator, allowing the user to select using letters. Each option should be related to foreshadowing in the text.
For possible non-original responses from the user, you need to flexibly adjust the subsequent storyline without disrupting the main plot.
The newly generated plot should not contain spoilers or excessive hints and should not introduce future characters or items from the script prematurely.
Please generate word in %s language.
"""

system_define_poet = "You are a world-class poet. Respond only with short poems."


def play(request: PlayRequest) -> str:
    result = build_context(request)
    context = result.play_context
    result = claude_text_generator(system_define_game_master % (context.game, context.language), context.messages)
    context.messages.append(Message(role='assistant', content=result))
    dump_2_file(context)
    return result