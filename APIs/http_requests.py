import requests

term = input("What would you like to search for? ")
url = "https://icanhazdadjoke.com/search"

res = requests.get(
    url, 
    headers={"Accept": "application/json"}
    ).json()

print(res)