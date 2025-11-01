name = input("What is your name? ")
print(f"{name}")
print(f"{name.upper()}")
print(f"{name.lower()}")
print(f"{name.title()}")
print(f"{name.replace("a","@")}")

import random

def DoInput():
    name = input("Input name: ")
    return name

def DoOutput(name):
    output = f"Hello my dear {name}"
    parts = list(output)
    randomized_parts = [ch.upper() if random.choice([True, False]) else ch.lower() for ch in parts]
    randomized_output = "".join(randomized_parts)
    print(randomized_output)

if __name__ == '__main__':
    name = DoInput()
    DoOutput(name)
