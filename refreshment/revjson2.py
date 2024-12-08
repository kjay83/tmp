import json

filename = "revjson2.json"


def using_only_dict():
    print(f"Proceeding writing...")
    data = {
        "age": 15,
        "name": "alian",
        "job": {
            "id": 1,
            "name": "dev",
            "salary": 1500000,
        },
    }
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=True))

    print(f"Proceeding reading...")
    with open(filename, 'r') as f:
        contents_JSON = f.read()

    contents = json.loads(contents_JSON)
    print(contents)
    print(f"job salary is {contents.get("job").get("salary")}")


def using_classes():
    class Fruits:
        def __init__(self, name="Banan", color="Red"):
            self.name = name
            self.color = color

        def __repr__(self):
            return f"{self.__dict__}"

    f1 = Fruits("Fraise", "Red")
    f2 = Fruits("Mango", "Green")
    data = ""
    print(f"type f1={type(f1)} and f1= {f1}")
    print(f"dict f1={type(f1.__dict__)} and f1Dict= {f1.__dict__}")
    print(f"Proceeding writing...")
    with open(filename, 'w') as f:
        f.write(json.dumps(f1.__dict__, indent=2, ensure_ascii=True))

    print(f"Proceeding reading...")
    with open(filename, 'r') as f:
        contents_JSON = f.read()

    contents = json.loads(contents_JSON)
    print(type(contents))
    f1_reloaded = Fruits(**contents)
    print(f1_reloaded)


if __name__ == '__main__':
    using_classes()
