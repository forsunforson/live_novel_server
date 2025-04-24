from custom_types.struct import PlayContext, PlayRequest
import json
import os

def dump_2_file(play_context: PlayContext):
    file_name = f'{play_context.game}{play_context.uid}{play_context.branch}.json'
    file_path = os.path.join('/tmp/user_file', file_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(play_context.dict(), f)
    
def read_from_file(play_request: PlayRequest) -> PlayContext:
    file_name = f'{play_request.game}{play_request.uid}{play_request.branch}.json'
    file_path = os.path.join('/tmp/user_file', file_name)
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as f:
        data = json.load(f)
        return PlayContext(**data)