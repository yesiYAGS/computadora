import requests

api_key = "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"
prompt = input("\n\nPregunta algo:")

headers = {
    "Authorization": f"Besrer {api_key}",
    "Content-type": "application/json",
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": 
    [
        {
            "role":"user",
            "content":prompt
        }
    ]
}
url = "https://api.openai.com/v1/chat/completions"

response = requests.post(url, headers=headers, json=data)

answer = response.json()['choice'][0]['message']['content']

print("\n", answer, "\n")