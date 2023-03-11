# import json
# f = open("file.json", "r", encoding="utf-8")
# content = f.readlines()
# print(content)
# f.close()
#
# d = {}
# for record in content:
#     x = record.split(": ")
#     d[x[0]] = x[1].rstrip()
# print(d)
#
# f = open("file.json", "w", encoding="utf-8")
# json.dump(d, f, ensure_ascii=False)
# f.close()
#__________________________________________________________
# import json
# f = open("file.json", "r", encoding="utf-8")
# content = json.load(f)
# f.close()
#
# for i, element in enumerate(content):
#     t = type(element)
#     if t == str:
#         content[i] += "!"
#     elif t in (int, float):
#         content[i] += 1
#     elif t == bool:
#         content[i] = not content[i]
#     elif t == list:
#         content[i] = content[i] + content[i]
#     elif t == dict:
#         content[i]["newkey"] = None
#     elif content[i] == None:
#         del content[i]
#
# print(json.dumps(content))
# _________________________________________________________
# import json
# f = open("file.json", "r", encoding="utf-8")
# content = json.load(f)
# f.close()
#
# print(content)
#
# #формирование списка атрибутов
# all_atributs = []
# for person in content:
#     for atrib in person:
#         if atrib not in all_atributs:
#             all_atributs.append(atrib)
#
# #print(all_atributs)
#
#
# for person in content:
#     for atrib in all_atributs:
#         if atrib not in person:
#             person[atrib] = None
#
# print(content)
#
# print(json.dumps(content, ensure_ascii=False))
#__________________________________________________________
import requests
responce = requests.get(url="http://api.open-notify.org/iss-now.json")
data = responce.json()['iss_position']
print(data)
print("широта: ", data['latitude'])
print("долгота: ", data['longitude'])























