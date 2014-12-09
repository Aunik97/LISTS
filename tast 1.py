first_student = input(print("Please enter the name of the first student:"))
second_student = input(print("Please enter the name of the second student: "))
third_student = input(print("Please enter the name of the third student: "))
fourth_student = input(print("Please enter the name of the fourth student: "))
fifth_student = input(print("Please enter the name of the fifth student: "))
sixth_student = input(print("Please enter the name of the sixth student: "))
seventh_student = input(print("Please enter the name of the seventh student: "))
eighth_student = input(print("Please enter the name of the eighth student: "))
students_list = first_student, second_student, third_student, fourth_student, fifth_student, sixth_student, seventh_student, eighth_student
for count in students_list:
    print(count)
student_name_change = str(input("Enter the new student name: "))
placeToChange = int(input("Enter where this student needs to be replaced: "))
students_list.insert(placeToChange,student_name_change)
for count in students_list:
    print(each)
