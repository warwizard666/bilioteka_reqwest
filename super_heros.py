import requests

#r = requests.get("https://netology.ru/")
#print(r.json())

url = "https://akabab.github.io/superhero-api/api/all.json"

response = requests.get(url)

data = response.json()
max_intelligence = 0
hero_with_max_intelligence = ""
for hero in data:
    name = hero["name"]
    intelligence = hero["powerstats"]["intelligence"]
    if name == "Hulk" or name == "Captain America" or name == "Thanos":
            if intelligence > max_intelligence:
                max_intelligence = intelligence
                hero_with_max_intelligence = name
print(f"Супергерой: {hero_with_max_intelligence}, Интеллект: {max_intelligence}")




