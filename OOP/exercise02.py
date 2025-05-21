# Teil a: Klasse Person
class Person:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def ausgabe(self):
        print(f"Name: {self.Name}, Alter: {self.Age}")

    # Teil b: Eingabe neue Werte
    def eingabe_neuer_daten(self):
        self.Name = input("Geben Sie den neuen Namen ein: ")
        self.Age = int(input("Geben Sie das neue Alter ein: "))


# Teil c: Klasse Personen (Containerklasse)
class Personen:
    def __init__(self):
        self.personen_liste = []

    def person_hinzufuegen(self, name, age):
        person = Person(name, age)
        self.personen_liste.append(person)

    def ausgabe_aller_personen(self):
        print("\nAlle Personen:")
        for p in self.personen_liste:
            p.ausgabe()


# Teil d: Fleißaufgabe – Kombinierte Klasse
class PersonenManager:
    def __init__(self):
        self.personen = []

    def neue_person(self):
        name = input("Name der Person: ")
        age = int(input("Alter der Person: "))
        person = Person(name, age)
        self.personen.append(person)

    def alle_ausgeben(self):
        print("\nPersonen im Manager:")
        for person in self.personen:
            person.ausgabe()

    def person_daten_bearbeiten(self, index):
        if 0 <= index < len(self.personen):
            self.personen[index].eingabe_neuer_daten()
        else:
            print("Ungültiger Index")


# Testcode (nur für interaktives Testen – entfernen oder abändern bei Import)
if __name__ == "__main__":
    # a + b
    p1 = Person("Max", 25)
    p1.ausgabe()
    p1.eingabe_neuer_daten()
    p1.ausgabe()

    # c
    gruppe = Personen()
    gruppe.person_hinzufuegen("Anna", 30)
    gruppe.person_hinzufuegen("Ben", 45)
    gruppe.ausgabe_aller_personen()

    # d
    manager = PersonenManager()
    manager.neue_person()
    manager.alle_ausgeben()
    manager.person_daten_bearbeiten(0)
    manager.alle_ausgeben()
