name_numbers = [input().split() for i in range(int(input()))]
name_dict = {a:b for a, b in name_numbers}
while True:
    try:
        name = input()
        if name in name_dict:
            print(f"{name}={name_dict[name]}")
        else:
            print("Not found")
    except EOFError:
        break