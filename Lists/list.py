hat_list = [1, 2, 3, 4, 5]

hat_list[2] = int(input("Enter a number to replace the middle element: "))

hat_list.pop()          
hat_list.append(123) 

print("Length of the list:", len(hat_list))
print("Sum of the list:", sum(hat_list))
