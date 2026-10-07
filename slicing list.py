#The format for list slicing is list_name[start: stop: step].

#start is the index of the list where slicing starts.
#stop is the index of the list where slicing ends.
#step allows you to select nth item within the range start to stop.
#List slicing works similar to Python slice() function.

#Get all the Items
my_list = [1, 2, 3, 4, 5]

print(my_list[:])


#If you simply use :, you will get all the elements of the list.
# This is similar to print(my_list).

#Get all the Items After a Specific Position
my_list = [1, 2, 3, 4, 5]

print(my_list[2:])


#If you want to get all the elements after a specific index,
# you can mention that index before : as shown in example above.

#In the above example, elements at index 2 and all the elements after index 2 are printed.

#Note: Indexing starts from 0. Item on index 2 is also included.

#Get all the Items Before a Specific Position
my_list = [1, 2, 3, 4, 5]

print(my_list[:2])

#This example lets you get all the elements before a specific index. Mention that index after :.

#In the example, the items before index 2 are sliced. Item on index 2 is excluded.

#Get all the Items from One Position to Another Position
my_list = [1, 2, 3, 4, 5]

print(my_list[2:4])

#If you want to get all the elements between two specific indices,
# you can mention them before and after :.

#In the above example, my_list[2:4] gives the elements between
# 2nd and the 4th positions. The starting position (i.e. 2) is included 
#and the ending position (i.e. 4) is excluded.

#Get the Items at Specified Intervals
my_list = [1, 2, 3, 4, 5]

print(my_list[::2])

#If you want to get elements at specified intervals, you can do it by using two :.

#In the above example, the items at interval 2 starting from index 0 are sliced.

#If you want the indexing to start from the last item, you can use negative sign -.

my_list = [1, 2, 3, 4, 5]

print(my_list[::-2])

#The items at interval 2 starting from the last index are sliced.

#If you want the items from one position to another, you can mention them from start to stop.

my_list = [1, 2, 3, 4, 5]

print(my_list[1:4:2])

#The items from index 1 to 4 are sliced with intervals of 2.

