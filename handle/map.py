from client.anthropic import claude_text_generator
from custom_types.struct import BaseRequest, PlayRequest, Message
from context.context_builder import build_context

system_define_map = """You are a game master. you need to describe available location for the player. Please generate word in %s language."""

def get_available_location(request: BaseRequest) -> str:
    play_request = PlayRequest(game=request.game, uid=request.uid, branch=request.branch, language=request.language, content='')
    context = build_context(play_request)
    context.messages.append(Message(role='user', content='generate a map for the me according to the history of the game.'))
    result = claude_text_generator(system_define_map % play_request.language, context.messages)
    return result
     