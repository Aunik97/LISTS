name1 = str(input("Enter the 1st name: "))
name2 = str(input("Enter the 2nd name: "))
name3 = str(input("Enter the 3rd name: "))
name4 = str(input("Enter the 4th name: "))
name5 = str(input("Enter the 5th name: "))
name6 = str(input("Enter the 6th name: "))
name7 = str(input("Enter the 7th name: "))
name8 = str(input("Enter the 8th name: "))
name_list = [name1, name2, name3, name4, name5, name6, name7, name8]
for every in name_list:
    print(every)
change = input("please enter the new student name: ")
position = int(input("please enter the position that the new student is replacing: "))
name_list[position] = change
for each in name_list:
    print(each)
