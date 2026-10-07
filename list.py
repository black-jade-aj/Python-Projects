thislist = ["Alice", "Bob", "Charlie"]
print(thislist)
print(len(thislist)) #for printing the length(number of items) of the list

lists = list(("Alice", "Bob", "Charlie"))
print(lists)

list = ["Alice", "Bob", "Charlie"]
print(list[2]) # for printing the item at index 2 of the list
#list indexing starts from 0, so index 2 is the third item in the list
#-1 refers to the last item, -2 refers to the second last item etc.

#Example
#Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range.

#When specifying a range, the return value will be a new list with the specified items.

#Example
#Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

  #A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]