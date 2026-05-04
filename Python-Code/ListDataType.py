#List is a data type which allows multiple values, and can have different types.
values = [1, 2, "Python",6.5, 'last value']

#For list index starts from 0. To print a value from list

print(values[0]) #Here Output will be '1'
print(values[3]) #Here Output will be '6.5'

#If we want to print the last value in a list, there is one short cut
print(values[-1]) #O/P: 'last. value'. Here -1 refers to the last index of a list

#To get the Sub-list values from a list
print(values[1:3]) #o/p: [2, 'Python']. Here it will fetch values of index 1 and 2, not index 3

#To insert "Programming" word after "Python in the List"
values.insert(3, 'Programming')
print(values)

#To add a new value at the end of the List, no matter how many values are there in the list, we can use 'append()'
values.append("End of List")
print(values)

#To update the value in a List for a particular index
values[3] = 'Learning'
print(values)

#To delete the value for a particular index in a list
del values[6]
print(values)