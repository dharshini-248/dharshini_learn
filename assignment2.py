import json

# Open the JSON file
with open('ex5.json') as file:
    # Load the JSON data
    data = json.load(file)

# Access the data
print(data)

print(type(data))

#storing as a dictionary
ex5 = {item['id']: item for item in data}

print(ex5)

print(type(ex5))

#to add a batter named Coffee for “donut” with name “Old Fashoined”

for item in data:
    if item["type"] == "donut" and item["name"] == "Old Fashioned":
        # Add a new batter named "Coffee" to the "batter" list
        item["batters"]["batter"].append({"id": "1005", "type": "Coffee"})

print(data)


#Replacing old json file with new data

with open('ex5.json', 'w') as file:
    json.dump(data, file)
    
print("Updated Json file data",data)