def greet_person(name):
    if isinstance(name, int):
        print("Numbers not allowed!")
    else:   
        print(f"Hello, {name}!")
