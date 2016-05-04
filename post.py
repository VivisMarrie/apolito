import requests, json

post_data = {
        "fase": 1,
        "aluno": 2,
        "tempo": 100,
        "tentativas": 2,
        "toques": [
            {
                "x": 100,
                "y": 200,
                "t": 2,
                "acao" : 2
            },
            {
                "x": 500,
                "y": 300,
                "t": 6,
                "acao" : 1
            },
            {
                "x": 400,
                "y": 800,
                "t": 8,
                "acao" : 5
            }
        ],
        "frustrado": False
    }
post_data = json.dumps(post_data)
response = requests.post('http://vivismarrie.pythonanywhere.com/app/', data=post_data)
content = response.content
print content