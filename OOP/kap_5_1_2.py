""" Klassen und Typattribute """

""" Beispiel für "Public"- Typattribut (Standard) """
class Bike:
    """ Eine Klasse zur Beschreibung eines Fahrrades """
    # Klassenattribute werden durch Instanzattribute gleichen Namens UEBERSCHRIEBEN.
    # class_weight = 10 # Klassenattribut
    def __init__(self, name, brand):
        self.name = name  # Instanzattribute
        self.brand = brand
        self.weight = 10

    def set_new_weight(self, new_weight):      # Methode zur Aenderung eines Attributes durch indirekten Zugriff
        if new_weight < 0:                     # Möglichkeit zur Prüfung vor Zuweisung
            print("Values below zero not allowed")
        else:
            self.weight = new_weight           # Variablenuebergabe "setter-Methode"

    def increment_weight(self):                # Methode zur Aenderung eines Attributes durch
        self.weight += 1                       # Inkrementieren

    def show_weight(self):                     # "getter-Methode"
        # self.increment_weight()
        return self.weight                     # return gibt lediglich Werte zurück, nicht die Objekte selbst

    def ring(self):                            # Methode "ring"
        print("ringing…")

    def shift_gear(self):
        print("shifting gear…")

# Class definition ready
# Now we can use this class, all it's methods (=functions) and attributes (= variables) 
# But first, the class needs to be instantiated !
my_bike_2 = Bike("CityGo2", "Bullet2")  # Instantiierung
# my_bike_2.ring()

# my_bike_2.set_new_weight(-21)
# print(my_bike_2.weight)
# my_bike_2.weight = 25
# print(my_bike_2.weight)
# print(dir(my_bike_2))
# my_bike_2.set_new_weight(21)
# print(my_bike_2.weight)
# my_bike_2.increment_weight()
# print(my_bike_2.weight)
# print(my_bike_2.show_weight())

# my_bike_3 = Bike("Titan", "CityGo")  # Instantiierung
# my_bike_3.ring()

# print(my_bike_2.weight)         # direkter Zugriff auf Instanzattribut von ausserhalb der Klasse
# my_bike_2.weight = 20
# print(my_bike_2.weight)         # direkter Zugriff auf Instanzattribut von ausserhalb der Klasse

# print(my_bike_2.show_weight())   # INDIREKTER Zugriff auf Instanzattribut durch "getter" Methode
# my_bike_2.weight = 15                      # direkter Zugriff auf Instanzattribut von ausserhalb der Klasse
# print("direkt:", my_bike_2.weight)         # direkter Zugriff auf Instanzattribut von ausserhalb der Klasse

# my_bike_2.set_new_weight(25)                # INDIREKTER Zugriff auf Instanzattribut durch "setter" Methode
# print("direkt:", my_bike_2.weight)          # direkter Zugriff auf Instanzattribut von ausserhalb der Klasse

# print("indirekt:", my_bike_2.show_weight())  # INDIREKTER Zugriff auf Instanzattribut durch "getter" Methode

# my_bike_2.increment_weight()                 # INDIREKTER Zugriff auf Instanzattribut durch "setter" Methode
# print("indirekt:", my_bike_2.show_weight())  # INDIREKTER Zugriff auf Instanzattribut durch "getter" Methode

# my_bike_2.increment_weight()                 # INDIREKTER Zugriff auf Instanzattribut durch "setter" Methode
# print("indirekt:", my_bike_2.show_weight())  # INDIREKTER Zugriff auf Instanzattribut durch "getter" Methode
# print("direkt:", my_bike_2.weight)          # direkter Zugriff auf Instanzattribut von ausserhalb der Klasse

""" Beispiel für Typattribute - Typ "Protected" """

# class Bike:
#     """ Eine Klasse zur Beschreibung eines Fahrrades """
    # Setzen eines Klassenattributes
    # _weight = 10 # Der Zugriff auf Klassenattribute ist ueber den Klassennamen oder den Instanznamen moeglich.
    # def __init__(self, name, brand):
    #     """Initialisiere Attribute: Namen und Hersteller"""
    #     self.name = name  # Instanzattribute
    #     self.brand = brand
    #     self._weight = 10 # Typattribut : "Protected"
    #
    # def set_new_weight(self, new_weight):  # Methode zur Aenderung eines Attributes durch
    #     self._weight = new_weight  # Variablenuebergabe "setter-Methode"
    #
    # def increment_weight(self):  # Methode zur Aenderung eines Attributes durch
    #     self._weight += 1  # Inkrementieren
    #
    # def show_weight(self):  # "getter-Methode"
    #     return self._weight
    #
    # def ring(self):  # einfache Methode (=funktion) "ring"
    #     print("ringing…")
    #
    # def shift_gear(self):
    #     print("shifting gear…")

# my_bike_2 = Bike("CityGo2", "Bullet2")  # Instantiierung
# print(my_bike_2._weight)           # direkter Zugriff auf Instanzattribut von ausserhalb der Klasse
#                                  # Verwendung von Variablen mit Typ "protected" weiterhin möglich, siehe Typ "public".
#                                  # Konvention besagt jedoch, daß Direkter Zugriff unterbleiben sollte.
# my_bike_2._weight = 25
# print(my_bike_2._weight)


""" Beispiel für Typattribute - Typ "Private """

# class Bike:
#     """ Eine Klasse zur Beschreibung eines Fahrrades """
#     # Setzen eines Klassenattributes
#     # __weight = 10 # Der Zugriff auf Klassenattribute ist ueber den Klassennamen oder den Instanznamen moeglich.
#     def __init__(self, name, brand):
#         """Initialisiere Attribute: Namen und Hersteller"""
#         self.name = name  # Instanzattribute
#         self.brand = brand
#         self.__weight = 10

    # def set_new_weight(self, new_weight):  # Methode zur Aenderung eines Attributes durch
    #     if not isinstance(new_weight,int):
    #         print("Only int allowed.")
    #         return
    #     if new_weight < 0:
    #         print("negative values are not allowed")
    #         return
    #     else:
    #         self.__weight = new_weight  # Variablenuebergabe "setter-Methode"

    # def increment_weight(self):  # Methode zur Aenderung eines Attributes durch
    #     self.__weight += 1       # Inkrementieren

    # def show_weight(self):  # "getter-Methode"
        # print(id(self.__weight))
        # return self.__weight

    # def ring(self):  # einfache Methode (=funktion) "ring"
    #     print("ringing…")

    # def shift_gear(self):
    #     print("shifting gear…")

# private Typattribute: Lesen und schreiben mit getter/setter-Methoden.

# my_bike_2 = Bike("CityGo2", "Bullet2")  # Instantiierung
# my_bike_2.ring()

# print(my_bike_2.__weight)         # direkter Zugriff auf Instanzattribut von ausserhalb der Klasse private GEHT NICHT!
# print(my_bike_2.show_weight())     # INDIREKTER Zugriff auf Instanzattribut durch "getter" Methode FUNKTIONIERT!
# print(dir(my_bike_2))
# print(my_bike_2._Bike__weight, type(my_bike_2._Bike__weight))
#
# my_bike_2.set_new_weight(25)                 # INDIREKTER Zugriff auf Instanzattribut durch "setter" Methode
# print("indirekt:", my_bike_2.show_weight())  # INDIREKTER Zugriff auf Instanzattribut durch "getter" Methode
# print("direkt:", my_bike_2.__weight, id(my_bike_2.__weight))         # direkter Zugriff auf Instanzattribut von ausserhalb der Klasse
#
# my_bike_2.increment_weight()                 # INDIREKTER Zugriff auf Instanzattribut durch "setter" Methode
# print("indirekt:", my_bike_2.show_weight())  # INDIREKTER Zugriff auf Instanzattribut durch "getter" Methode
#
# my_bike_2.increment_weight()                 # INDIREKTER Zugriff auf Instanzattribut durch "setter" Methode
# print("indirekt:", my_bike_2.show_weight())  # INDIREKTER Zugriff auf Instanzattribut durch "getter" Methode
#
# print("direkt:", my_bike_2.__weight, id(my_bike_2.__weight))         # direkter Zugriff auf Instanzattribut von ausserhalb der Klasse SCHEINERFOLG
#
# direkter Zugriff von ausserhalb der Klasse auf Instanzattibute vom Typ "private" funktioniert NICHT.
# Zugriff nur noch durch "setter" und "getter" Methoden.

# my_bike_3 = Bike("CityGo3", "Bullet3")  # Instantiierung

# Name mangling: Im Ausnahmefall ist der direkte Zugriff immer noch möglich.
# print(my_bike_2._Bike__weight) # direkter Zugriff auf private Variablen ist unter einer ANDEREN ADDRESSE IMMER NOCH MÖGLICH.
# my_bike_2._Bike__weight = 100 # direkter Zugriff auf private Variablen ist unter einer ANDEREN ADDRESSE IMMER NOCH MÖGLICH.
# print(my_bike_2._Bike__weight)# , id(my_bike_2._Bike__weight)) # direkter Zugriff auf private Variablen ist unter einer ANDEREN ADDRESSE IMMER NOCH MÖGLICH.
# print(my_bike_2.show_weight())

"""
#################
# Typattribute: #
#################
# public        # 
# _protected    #
# __private     #
#################
"""

""" 
- Vererbung und Subklassen (Kind-Klassen) 
- Inheritance and Subclassing (Child classes)  
"""

class Gravelbike(Bike):                      # parent class name in brackets
    def __init__(self, name, brand, price):  # Setzt die Werte aller Argumente der Eltern- und Kind-Klassen
        super().__init__(name,brand)        # Setzt die Kind-Klasse mit der Elternklasse in Verbindung
        # Bike.__init__(self,name, brand)     # Setzt die Kind-Klasse mit der Elternklasse in Verbindung
        self.tiresize = 29                   # Ab hier können neue Methoden und Attribute definiert
        self.framesize = 54                  # werden, welche nur für die Klasse “gravelbike“ gelten.
        self.price = price
        self.frame_weight = 11
        # print("self.__class__ attribute: ",self.__class__)

    def ring(self):  # Ueberschreiben einer gleichnamigen Methode der Eltern-Klasse
        print("dingdong…")

    def set_new_weight(self, new_weight):  # Methode zur Aenderung eines Attributes durch
        self.frame_weight = new_weight       # Variablenuebergabe (setter-Methode)

    def increment_weight(self):            # Methode zur Aenderung eines Attributes durch
        self.frame_weight += 2               # Inkrementieren (setter-Methode)

    def show_weight(self):                 # getter-Methode
        return self.frame_weight

    def show_parent_weight(self):
        return self.weight

my_gb2 = Gravelbike("Burley", "ProMax",1899) # Erzeuge Instanz namens "my_gb2"
print(my_gb2, type(my_gb2))

# my_gb2.ring()
# print(my_gb2.show_parent_weight())
# print(my_gb2.show_weight())
#
# print(isinstance(my_gb2,Gravelbike))
# print(issubclass(Gravelbike,Bike))
# print(isinstance(my_gb2,Bike))

# print(my_gb2.name, my_gb2.brand, my_gb2.price)
# my_gb2.ring()
# my_gb2.shift_gear()

# b2 = Bike("Scott", "Burley")
# b2.ring()
# my_gb2.ring()
# print(my_gb2.framesize)
# print(dir(my_gb2))

""" dynamische Erzeugung von Instanzen und Verwaltung in Listen """

# nlist = ["Scott","Burley","Pegasus"]
# clist = []
# for i in nlist:
#     clist.append(Gravelbike(i, "Bullet", 1299))  # Erzeuge Instanz als Listeneintrag
# print(clist)
#
# for i in clist:
#     print(i.name, i.brand)

# print(clist[0].name)
# clist[0].ring()
#
# delete method from single inheritance instance by overwriting

# def show_parent_weight():
#     print("Method disabled")
#     pass

# my_gb2.show_parent_weight = show_parent_weight # redefining attribute
# my_gb2.show_parent_weight()

# print(dir(clist[0]))
# my_gb = Gravelbike("Scott", "Bullet", 1299)  # Erzeuge Instanz namens "my_gb"
# print(dir(my_gb),type(my_gb))
# print("Subclass gravelbike")
# print("Tiresize: ", my_gb.tiresize)
#
# print(my_gb.show_weight())
# my_gb.increment_weight()
# print(my_gb.show_weight())
# my_gb.increment_weight()
# print(my_gb.show_weight())
# print(my_gb.price)
# my_gb.ring1()
# my_gb.ring()
# my_gb.shift_gear()
# print(my_gb.name)
# print(my_gb.brand)