import json
from typing import Dict
import requests

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
if __name__ == "__main__":
    print(data.get("researcher").get("relatives"))

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    print(type(response))
    todos : list = json.loads(response.text)
    # {
    # "userId": 1,
    # "id": 1,
    # "title": "delectus aut autem",
    # "completed": false
    # }
    filtre={}
    for todo in todos:
        if todo['completed']:
            nbCompletedTask = filtre.get(todo["userId"])
            if nbCompletedTask == None:
                filtre.update({todo["userId"] : 1})
            else:
                filtre.update({todo["userId"] : nbCompletedTask+1})
            print(f"Todo N° {todo["id"]} COMPLETED by userID {todo["userId"]}, it is his {filtre.get(todo["userId"])} success!")
    
    print(f"results are: {filtre}")
    max=0
    for user,nb in filtre.items():
        if max < nb:
            max=nb
    bestUser=[user for user,nb in filtre.items() if max==nb]
    # for user,nb in filtre.items():
    #     if max == nb:
    #         bestUser.append(user)
    print(f"Le(s) meilleur(s) user(s) est(sont) {bestUser} avec {max} task(s) completed!!")
    