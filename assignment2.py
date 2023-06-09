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