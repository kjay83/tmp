import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE+"videos/111",{"likes":25,"erer":800, "name":"Yuna"})
# print("videos test : "+str(response.json()))
print("in test.py")
print(response.json())

# response = requests.get(BASE + "pple/timora")
# print("pple test get : "+str(response.json()))

# response = requests.get(BASE + "hello")
# print("get"+str(response.json()))

# response = requests.post(BASE + "hello")
# print("post"+str(response.json()))

# response = requests.put(BASE + "hello")
# print("put"+str(response.json()))

# response = requests.delete(BASE + "hello")
# print("delete"+str(response.json()))

