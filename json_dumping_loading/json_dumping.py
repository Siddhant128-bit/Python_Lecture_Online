import json

date_to_write={
    'name': "Siddhant Sharma",
    'age': '100',
    'city': 'ABC',
}


#How to write it as json file from dictionary

with open('data.json','w') as f:
    json.dump(date_to_write,f)


