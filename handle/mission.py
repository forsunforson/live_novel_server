from client.anthropic import claude_text_generator
from custom_types.struct import BaseRequest, PlayRequest, Message
from context.context_builder import build_context

system_define_mission_abstract = """You are a game master. you need to generate a game mission for the player. Please generate word in %s language."""

def get_all_mission(request: PlayRequest) -> str:
    result = build_context(request)
    if result.is_new_game is True:
        return "no available mission"
    context = result.play_context
    context.messages.append(Message(role='user', content='generate a game mission for the me according to the history of the game.'))
    result = claude_text_generator(system_define_mission_abstract % request.language, context.messages)
    return result
     