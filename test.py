#Aunik Hussain
#12/01/15






def linear_search(search_list, search_item):
    found = False
    index = 0
    while not found and index < len(people):
        if search_list == people[index]:
            print("Found")
            found = True
        else:
            print("Not Found")
            index = index + 1
        return found

def bubble_sort(people):
    for index in range(len(people)):
        for item in range(index):
            if people[item] > people[item + 1]:
                temp = people[item]
                people[item] = people[item + 1]
                people[item + 1] = temp
            
                       




def test():
    people = ["Aunik", "Harry", "Matt", "Ben", "Dan", "Indi", "John"]
    sorted_list = bubble_sort(people)
    print(sorted_list)
    
                          
    
    
    
    
    

#Main

people = ["Aunik", "Harry", "Matt", "Ben", "Dan", "Indi", "John"]

search_item = input("enter a name")
search_list = search_item
linear_search(search_list, search_item)
done = bubble_sort
bubble_sort(people)
test()
print(people)
















       # if unsorted[index]> unsorted[index + 1]:
       #     temp = unsorted[index]
       #     unsorted[index] = unsorted[index +1]
      #      unsorted[index + 1] = temp
      #      done = True
      #  index = index + 1
   # sorted_list = unsorted
   # return sorted_list



    
    
