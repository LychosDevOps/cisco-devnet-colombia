import yaml
import json

with open('directorio.yml') as data:
    data_directorio = data.read()

# print(data_directorio)

directorio = yaml.load(data_directorio)
print(json.dumps(directorio, indent=4))