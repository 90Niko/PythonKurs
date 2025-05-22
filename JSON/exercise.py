import json

class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def toJson(self):
        return json.dumps(self.__dict__, indent=4)

class Familie:
    def __init__(self, vater, mutter, kinder):
        self.vater = vater
        self.mutter = mutter
        self.kinder = kinder

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

# Personen erstellen
vater = Person('Peter', 35)
mutter = Person('Maria', 33)
sohn = Person('Paul', 3)
tochter = Person('Anna', 5)

# Kinderliste
kinder = [tochter, sohn]

# Familie erstellen
familie = Familie(vater, mutter, kinder)

# Vater in JSON-Datei speichern
with open("test_vater.json", "w") as v:
    v.write(vater.toJson())

# Familie in JSON-Datei speichern
with open("test_familie.json", "w") as f:
    f.write(familie.toJson())

print('Fertig')
