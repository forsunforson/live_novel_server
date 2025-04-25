from client.anthropic import claude_text_generator
from custom_types.struct import BaseRequest, PlayRequest, Message
from context.context_builder import build_context

system_define_mission_abstract = """You are a game master. you need to generate a game mission for the player. Please generate word in %s language."""

def get_all_mission(request: BaseRequest) -> str:
    play_request = PlayRequest(game=request.game, uid=request.uid, branch=request.branch, language=request.language, content='')
    print(play_request)
    context = build_context(play_request)
    context.messages.append(Message(role='user', content='generate a game mission for the me according to the history of the game.'))
    result = claude_text_generator(system_define_mission_abstract % play_request.language, context.messages)
    return result
     