from custom_types.struct import BaseRequest


def check_params(request: BaseRequest) -> bool:
    if request.game is None or request.game == '':
        return False
    if request.uid is None or request.uid == '':
        return False
    if request.branch is None or request.branch == '':
        return False
    return True