import requests

print('hello world')


url = "https://api.adviceslip.com/advice"

Data = requests.get(url)
json_data = Data.json()
print(json_data)


random_advice = json_data["slip"]
print("\n")
print("\n")
print(random_advice["advice"])
