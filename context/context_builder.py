from storage.file_storage import read_from_file
from custom_types.struct import Message, PlayContext, PlayRequest

round_one_message = """
To start the game:
Explain the game rules to me.
Let me choose a character from a list you provide, with a brief summary of each character's traits.
Once I have chosen, we can begin the game from the start of the script.
"""

class ContextResult:
    def __init__(self, play_context: PlayContext, is_new_game: bool) -> None:
        self.play_context = play_context
        self.is_new_game = is_new_game

def build_context(play_request: PlayRequest) -> ContextResult:
    play_context = read_from_file(play_request)
    if play_context is None:
        play_context = PlayContext(game=play_request.game, uid=play_request.uid, branch=play_request.branch, language=play_request.language, messages=[Message(role='user', content=round_one_message)])
        return ContextResult(play_context, True)
    else:
        play_context.messages.append(Message(role='user', content=play_request.content))
        return ContextResult(play_context, False)