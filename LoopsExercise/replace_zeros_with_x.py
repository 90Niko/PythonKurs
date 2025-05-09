modified_string = ""

for digit in "0165031806510":
    if digit == "0":
        modified_string += "x"
        continue
    modified_string += digit

print(modified_string)
