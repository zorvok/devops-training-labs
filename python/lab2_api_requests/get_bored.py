import requests
r = requests.get("https://www.boredapi.com/api/activity")
print("Activity:", r.json()["activity"])