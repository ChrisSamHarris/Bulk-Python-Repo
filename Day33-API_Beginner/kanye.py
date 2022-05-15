import requests

def get_quote():
    kanye_response = requests.get(url="https://api.kanye.rest")
    kanye_response.raise_for_status()
    quote = kanye_response.json()['quote']
    print(f"\n{quote}\n")

get_quote()
