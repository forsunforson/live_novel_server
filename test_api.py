import requests


PLAY_URL = 'http://localhost:8000/play'


# 测试 POST 请求
def test_play_post():
    data1 = {
        'game': 'example_game',
        'uid': 'example_uid',
        'branch': 'example_branch',
        'language': 'zh',
        'content': 'example_content'
    }
    response = requests.post(PLAY_URL, json=data1)
    assert response.json()["status_code"] == 200
    
    data2 = {
        'game': 'example_game',
        'branch': 'example_branch',
        'uid': '',
        'content': '你是谁'
    }
    response = requests.post(PLAY_URL, json=data2)

    assert response.json()["status_code"] == 400

def test_mission():
    data = {
        'game': 'example_game',
        'uid': 'example_uid',
        'branch': 'example_branch',
        'language': 'zh',
    }
    response = requests.get('http://localhost:8000/mission', json=data)
    assert response.status_code == 200

if __name__ == '__main__':
    test_play_post()
    test_mission()