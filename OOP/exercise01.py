class Hund:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def bark(self):
       return f"{self.name} bellt sehr laut!"

mein_hund = Hund("Bello", 3)

print()
print(f"Mein Hund heißt {mein_hund.name}, er ist {mein_hund.age} Jahre alt und {mein_hund.bark()}.")
print()
