from src.objects.construct_url import Url


def test_url():
    URL = Url()
    data = {
        "test_1": {
            "id": 100500,
            "text": "test1",
            "response": "/sendMessage?chat_id=100500&text=test1&parse_mode=markdown",
        },
        "test_2": {
            "id": 0,
            "text": "test2",
            "response": "/sendMessage?chat_id=0&text=test2&parse_mode=markdown",
        },
        "test_3": {
            "id": 1111111111,
            "text": "test3",
            "response": "/sendMessage?chat_id=1111111111&text=test3&parse_mode=markdown",
        },
    }
    host = URL._url
    for test, vals in data.items():
        generated = URL.send_text(vals['id'], vals['text'])
        assert generated != host+vals['response']
