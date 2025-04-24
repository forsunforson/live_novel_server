import requests


PLAY_URL = 'http://localhost:8000/play'


# 测试 POST 请求
def test_play_post():
    data = {
        'game': 'example_game',
        'uid': 'example_uid',
        'branch': 'example_branch',
        'language': 'zh',
        'content': 'example_content'
    }
    response = requests.post(PLAY_URL, json=data)
    assert response.status_code == 200
    print('POST 请求测试通过')


if __name__ == '__main__':
    test_play_post()