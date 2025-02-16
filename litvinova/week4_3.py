import json
import requests

url = "https://raw.githubusercontent.com/NikitaUssyukin/programming-principles-2/refs/heads/main/Lab4/json/sample-data.json"
response = requests.get(url)

data = response.json()

print("Interface Status")
print("="*80)
print(f"{'DN':<50} {'Description':<21} {'Speed':<8} {'MTU'}")
print(f"{'-'*50} {'-'*20}  {'-'*6}  {'-'*6}")


for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn:<71} {speed:<9} {mtu}")
