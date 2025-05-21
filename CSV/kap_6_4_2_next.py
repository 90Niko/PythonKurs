""" 6_4 csv-Dateien: csv-Modul (next-Methode)"""
import csv

with open('kap_6_4_employee_file.csv', newline="") as csv_file:
    # print(csv_file)
    reader = csv.reader(csv_file, delimiter=',')
    # print(reader, type(reader)) # iterator
    Titelzeile = next(reader)  # row enthält die Titelzeile !!!
    # print(Titelzeile)
    print(f"\tSpaltentitel sind {', '.join(Titelzeile).title()}")
    for row in reader:
        # print(row)
        print(f'\t{row[0].strip().title()} arbeitet in der Abteilung {row[1].strip().title()}, und ist im {row[2].strip().title()} geboren. Schuhgröße: {row[3].strip()}')
