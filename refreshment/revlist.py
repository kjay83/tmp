people: list[str] = ['john','cathy','cassandra','albertostupert','ruronike','juinindo',200]

def get_long_names(l:list[str]) -> list[str]:
    result: list[str] = []
    for p in l:
        if len(p)<6:
            result.append(p)
    return result

long_names: list[str] = [p for p in people if len(p)<6]

if __name__ == "__main__":
    print(get_long_names(people))
    print(f"long names 2 ={long_names}")