""" 6_4 csv-Dateien: csv-Modul (line-num-Methode)"""
import csv

with open('kap_6_4_employee_file.csv', newline="", mode = "r") as f:  # csv Modul benoetigt den Parameter 'newline = ""'
    # print(f)
    reader = csv.reader(f, delimiter = ',')  # delimiter ist das Trennzeichen
    # print(reader)                          # "iterator" : iterierbares Objekt
    # print(dir(reader))
    # print(reader.line_num)
    # print(dir(reader.dialect))
    # print(reader.dialect.delimiter)
    for row in reader:                    # csv_reader ist ein "iterator"; iterator = iter(iterable)
        # print(row)
        # print(reader.line_num)
        if reader.line_num == 1:
            print(f"\tSpaltenüberschriften sind: {', '.join(row).title()}")
        else:
            print(f'\t{row[0].strip()} arbeitet in der Abteilung {row[1].strip()}, und ist im {row[2].strip()} geboren. Schuhgröße: {row[3].strip()}')
print(f"Bearbeitet: {reader.line_num} Zeilen.")

# Schreiben einer csv-Datei
# with open('kap_6_4_employee_file_res.csv', mode = 'w', newline="") as employee_file:
#     writer = csv.writer(employee_file, delimiter=',', quotechar = '"')
    # print(writer, dir(writer))
    # writer.writerow(['name','abteilung','geburtsmonat', 'shoesize'])
    # writer.writerow(['Claus, Schmidt ', 'Buchhaltung   ', 'November    ',38])
    # writer.writerow(['Herta Kleber', 'IT', 'Maerz   ',42])
    # writer.writerow(['Clemens Matulla   ', '    Engineering', 'Mai',41])
    # # # Alternative : "writerows"
    # data = [['name', 'abteilung', 'geburtsmonat', 'shoesize'], ['Claus Schmidt ', 'Buchhaltung', 'November', 38],
    #         ['Herta Kleber, ', 'IT', 'Maerz   ', 42], ['Clemens Matulla   ', '    Engineering', 'Mai', 41]]
    # writer.writerows(data)

# print(dir(writer))
# d = writer.dialect
# print(d)
# print(dir(d))
# print(d.delimiter)
# print(d.quotechar)
#
# print(csv.list_dialects())
# e = csv.get_dialect("excel")
# print(e, dir(e))
# print(e.delimiter, e.quotechar)
# print(e.escapechar, e.quoting)

# with open('kap_6_4_employee_file_res.csv', 'w', newline="") as employee_file:
#     writer = csv.writer(employee_file, dialect = "excel")
#     data = [['name,', 'Abteilung', 'geburtsmonat ', 'Shoesize'], ['Claus Schmidt ', 'Buchhaltung', 'November', 38],
#            ['Herta Kleber', 'IT', 'Maerz.;,   ', 42], ['Clemens Matulla   ', '    Engineering', 'Mai', 41]]
#     writer.writerows(data)
