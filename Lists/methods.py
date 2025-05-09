beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for i in range(2):
    new_member = input("Add another early member (Stu Sutcliffe or Pete Best): ")
    beatles.append(new_member)

beatles.pop()
beatles.pop()
beatles.reverse()

beatles.append("Ringo Starr")
beatles.reverse()

print("Final Beatles line-up:", beatles)
