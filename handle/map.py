from client.anthropic import claude_text_generator
from custom_types.struct import BaseRequest, PlayRequest, Message
from context.context_builder import build_context

system_define_map = """You are a game master. you need to describe available location for the player. Please generate word in %s language."""

def get_available_location(request: PlayRequest) -> str:
    result = build_context(request)
    if result.is_new_game is True:
        return "no available location"
    context = result.play_context
    context.messages.append(Message(role='user', content='generate a map for the me according to the history of the game.'))
    result = claude_text_generator(system_define_map % request.language, context.messages)
    return result
     