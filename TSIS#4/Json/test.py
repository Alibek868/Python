import json

file_path = "c:/Users/kozha/Desktop/Bored/Python/TSIS#4/Json/sample-data.json"

with open(file_path, "r") as f:
    data = json.load(f)
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    if 'name' in attributes and 'ID' in attributes:
        print(attributes['name'], attributes['ID'])
    else:
        print("'name' or 'ID' key not found in attributes.")
