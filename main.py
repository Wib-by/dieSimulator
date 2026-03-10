from random import randint
prim = input("""Welcome to Die Simulator

Enter a limit (Default - 6): """)
try:
    limit = int(prim)
    result = randint(1, limit)
    print(result)
except ValueError:
    if limit == "":
        result = randint(1, 6)
        print(result)
    else:
        print("User error - invalid input")