import json

with open('dados.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
print(data)
dados = json.loads(data)

cotista = dados["cotista"]
universal = dados["universal"]

print(cotista)
print(universal)