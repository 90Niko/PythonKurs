import json

# json.load()	Зарежда JSON от файл и го преобразува в Python обект.
# json.loads()	Зарежда JSON от низ (string) и го преобразува в Python обект.
# json.dump()	Записва Python обект в JSON файл.
# json.dumps()	Преобразува Python обект в JSON низ (string).

# data = {
#     "name": "Nikolay",
#     "age": 34
# }

# json_output = json.dumps(data, indent = 4)
# print(json_output)

# -----------------------

# json_string = '[{"name": "Nikolay", "age": 34}, {"name": "Maria", "age": 28}]'
# data = json.loads(json_string)

# for item in data:
#     print(item)

# -----------------------  

data = [
    {"name": "Nikolay", "age": 34},
    {"name": "Maria", "age": 28}
]

for person in data:
    print(f"{person['name']} is {person['age']} years old.")