#for index in range(len(people)):
   #     for item in range(index):
    #        if people[item] > people[item + 1]:
     #           temp = people[item]
      #          people[item] = people[item + 1]
      #          people[item + 1] = temp

people = ["d","a","b","c"]
for index in range(len(people)):
    for item in range(index):
        if people[item] > people[item + 1]:
            print(index)

            
