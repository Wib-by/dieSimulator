from random import randint
prim = input("""Welcome to Die Simulator

Enter a limit (Default - 6): """)
try:
    limit = int(prim)
    result = randint(1, limit)
    print(f"\n{result}")
except ValueError:
    if prim == "":
        result = randint(1, 6)
        print(f"\n{result}")
    else:
        print("User error - invalid input")