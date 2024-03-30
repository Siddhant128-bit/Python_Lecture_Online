import json

with open('data.json','r') as f:
    data_dictionary=json.load(f)


print(data_dictionary)