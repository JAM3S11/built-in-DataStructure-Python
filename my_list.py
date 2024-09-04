## create an empty list
my_list = []

# append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert() elements at specific index
my_list.insert(2, 15)

# extend() elements from another list
my_list.extend([50, 60, 70])

# remove() elements from the list
my_list.remove(70)

# sort() the list in ascending order
my_list.sort()

# find and print value of an element
print(my_list.index(30))