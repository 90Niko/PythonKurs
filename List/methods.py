# beatles = []

# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")

# for i in range(2):
#     new_member = input("Add another early member (Stu Sutcliffe or Pete Best): ")
#     beatles.append(new_member)

# beatles.pop()
# beatles.pop()
# beatles.reverse()
# print("Reverse Beatles line-up:", beatles)

# beatles.append("Ringo Starr")
# beatles.reverse()

# print("Final Beatles line-up:", beatles)

source_list = [1, 3, 2, 3, 4, 1, 5, 6, 2, 6, 7]


unique_list = []

for number in source_list:
    if number not in unique_list:
        unique_list.append(number)

print("Original list:", source_list)
print("List after removing duplicates:", unique_list)


