names = []
for number in range(8):
    names.append(input("Insert a name"))
number = int(input("insert a number: "))
names[number] = input("insert final name")
for each in names:
    print(each)
