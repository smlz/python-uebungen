import json

# Einfaches Beispiel
with open("name.json", "w") as f:
    name = "Rahel"
    json.dump(name, f)

with open("name.json") as f:
    gelesener_name = json.load(f)

print("Geschrieben haben wir:", name)
print("Und gelesen haben wir:", gelesener_name)

# Komplizierteres Beispiel
with open("person.json", "w") as f:
    person = {
        "name": "Rahel",
        "alter": 17,
        "hobbies": ["Fussball", "Trap"],
    }
    json.dump(person, f)

with open("person.json") as f:
    gelesene_person = json.load(f)

def print_person(person):
    print(f" - Name: {person['name']}")
    print(f" - Alter: {person['alter']}")
    print(" - Hobbies:")
    for hobby in person["hobbies"]:
        print(f"    * {hobby}")

print("Ursprüngliche Person:")
print_person(person)

print("Gespeicherte und gelesene Person:")
print_person(gelesene_person)

# Und gleich noch einmal:
with open("person2.json", "w") as f:
    json.dump(person, f, indent=4)


