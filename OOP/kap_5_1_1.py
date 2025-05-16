""" Kap. 5_1: Objektorientierung: Klassen """

print(dir())
class Sample: # Klammern sind hier optional, Klassenname immer mit Großbuchstaben
    # """ Eine einfache Klasse"""
    def __init__(self):
        self.x = 1
        
print(dir())

# print(dir()) # enthält Name der Klasse
# print(dir(Sample)) # enthält Name der Klasse

sample = Sample() # Instantiierung der Klasse ruft autmatisch die __init__ Methode auf,
# welche die Attribute erzeugt, welche an die Instanz gebunden sind.
# print(dir()) # enthält Name der Klasse und Name des Objektes
# print(dir(sample)) # enthält "x"

# print(sample.x) # Zugriff auf das Instanzattribut "x"

class Bike:    # Klammern sind hier optional
    """ Eine Klasse zur Beschreibung eines Fahrrades """
    # Klassenattribut hier (dieses Attribut wird von der Klasse und ALLEN INSTANZEN geteilt, hier kaum verwendet)
    # b = 10
    def __init__(self, name, brand):
        # Initialisiere Attribute: Namen und Hersteller (Instanzattribute hier)
        self.name = name
        self.brand = brand
        self.a = 20

    def ring(self):
        print("ringing …")
        # print(f"self.a: {self.a}")
        # print(f"self.name: {self.name}")
        # self.shift_gear()

    def shift_gear(self):
        print("shifting gear …")

    def print_value(self, value):
        print(f"print_value liefert: {value}")


my_bike = Bike("4Runner", "Cube")  # Instantiierung ESSENTIELL!
# ERST JETZT ist die Klasse komplett !!!!
# print(my_bike, type(my_bike))
# print(isinstance(my_bike,Bike))

# print(dir())
# print(dir(Bike)) # Klasse
# print()
# print(dir(my_bike)) # Instanz der Klasse

# print(my_bike.name) # Attributzugriff über Instanznamen
# print(my_bike.brand)
# print(my_bike.a)
#
# my_bike.ring()        # Methodenzugriff über den Instanznamenprint(my_bike.x)
# my_bike.shift_gear()
# my_bike.print_value("Hallo Python")

""" Instanzattribute und Klassenattribute """

# print(f" Instanzattribut a über Klassennamen: {Bike.a} (geht nicht)")    # Instanzattribut ist über den Instanznamen erreichbar,
# print(f" Instanzattribut a über Instanznamen: {my_bike.a}")              # Instanzattribut ist über den Instanznamen erreichbar,

# print(f" Klassenattribut b über Klassennamen: {Bike.b}")    # Klassenattribute sind über Klassennamen UND Instanznamen zugänglich
# print(f" Klassenattribut b über Instanznamen: {my_bike.b}") # Klassenattribute sind über Klassennamen UND Instanznamen zugänglich

my_bike2 = Bike("CitiGo", "Scott")                          # Instantiierung einer weiteren Instanz
# print(my_bike2,type(my_bike2), id(my_bike2))                # Klasseninstanz "my_bike2" kann nun verwendet werden.

# print(my_bike2.name)
# print(my_bike2.brand)
# print(my_bike2.a)
#
# my_bike2.ring()
# my_bike2.shift_gear()
# my_bike2.print_value("Hallo Python2")

# print(my_bike.a)
# my_bike.a = 40
# print(my_bike.a)
# print(my_bike2.a)

# print(my_bike2.a)      # Instanzattribute sind voneinander unabhängig
# print(my_bike.name)
# print(my_bike2.name)
# my_bike.name = "Newname"
# print(my_bike.name)
# print(my_bike2.name)

# print(Bike.b)
# print(my_bike.b)
# print(my_bike2.b)
#
# Bike.b = 100
# print(Bike.b)
# print(my_bike.b)
# print(my_bike2.b)

# Klassenattribute sind NICHT voneinander unabhängig
# print(f" Klassenattribut b über Klassennamen: {Bike.b}") # Klassenattribute sind über Klassennamen UND Instanznamen zugänglich
# print(f" Klassenattribut b über Instanznamen myBike: {my_bike.b}") # Klassenattribute sind über Klassennamen UND Instanznamen zugänglich
# print(f" Klassenattribut b über Instanznamen myBike2: {my_bike2.b}") # Klassenattribute sind über Klassennamen UND Instanznamen zugänglich

# Klassenattribute sind bei der Erstellung zunächst NICHT voneinander unabhängig
# Bike.b = 50
#
# print(f" Klassenattribut b über Klassennamen: {Bike.b}") # Klassenattribute sind über Klassennamen UND Instanznamen zugänglich
# print(f" Klassenattribut b über Instanznamen myBike: {my_bike.b}") # Klassenattribute sind über Klassennamen UND Instanznamen zugänglich
# print(f" Klassenattribut b über Instanznamen myBike2: {my_bike2.b}") # Klassenattribute sind über Klassennamen UND Instanznamen zugänglich

# print(f" Instanzattribut a über Klassennamen: {Bike.a}")
# print(f" Instanzattribut a über Instanznamen myBike: {my_bike.a}") # Klassenattribute sind über Klassennamen UND Instanznamen zugänglich
# print(f" Instanzattribut a über Instanznamen myBike2: {my_bike2.a}") # Klassenattribute sind über Klassennamen UND Instanznamen zugänglich

# my_bike.a = 40

# print(f" Instanzattribut a über Instanznamen myBike: {my_bike.a}") # Klassenattribute sind über Klassennamen UND Instanznamen zugänglich
# print(f" Instanzattribut a über Instanznamen myBike2: {my_bike2.a}") # Klassenattribute sind über Klassennamen UND Instanznamen zugänglich

print("Zugriff von ausserhalb:", my_bike.a)
my_bike.a = 40
print("Zugriff von aussen (geändert):", my_bike.a)

# my_bike2.print_value("Hallo, Python")

# my_bike.shift_gear()
# my_bike2.shift_gear()
