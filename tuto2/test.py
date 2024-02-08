import requests

BASE = "http://127.0.0.1:5000/"
uri="videos/222"
url = BASE + uri
response = requests.put(url,{"name":"Yuna4","likes":2150,"erer":800,"views":58 })
# print("videos test : "+str(response.json()))
print("in test.py")
print(response.json())
# input()
# response = requests.get(url)
# print(response.json())


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

