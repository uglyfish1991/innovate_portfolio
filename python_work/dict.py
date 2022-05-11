pet = {       #curly brackets / braces sets a dictionary
    "name": "Toby",     #keys and values, split with a colon
    "age": 2.5,
    "breed": "Keeshond",
    "favourite food": "plain Jacob's crackers",
    "best trick": "spin",
    "favourite toy": "moo cow",
    "favourite place": "any place with grass"
}

print(pet)    #call the dictionary
print(pet["name"])    # return the value of that key
print(pet["best trick"]) # return the value of that key

pet["best trick"] = "leave it"   #update the value of a key

print(pet["best trick"])

print(pet.keys())

print(pet.get("name"))

for i in pet.keys():
    print(i)

for i in pet.values():
    print(i)

thing=pet.pop("best trick")

print(type(thing))

