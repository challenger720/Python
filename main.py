name = input("What is your name? ")
print(f"{name}")
print(f"{name.upper()}")
print(f"{name.lower()}")
print(f"{name.title()}")
print(f"{name.replace("a","@")}")

 File "c:\Users\Janice\CSOH\random.py", line 16, in <module>
    DoOutput(name)
    ~~~~~~~~^^^^^^
  File "c:\Users\Janice\CSOH\random.py", line 10, in DoOutput
    randomized_parts = [ch.upper() if random.choice([True, False]) else ch.lower() for ch in parts]
                                      ^^^^^^^^^^^^^
AttributeError: module 'random' has no attribute 'choice' (consider renaming 'c:\Users\Janice\CSOH\random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)
