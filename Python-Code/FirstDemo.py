print("Hello, this is first Python Program.")

# we can start with hash and then write any comments in the python file

# Simple way of creating variable in Python
a = 3
print(a)

str = "Hello World"
print(str)

#we can actually define multiple variables in a single line
b,c, d = 5, 6.4, "Great"

#print("Value is: " + b) #This will not allow in Python, it will throw an error saying 'TypeError: can only concatenate str (not "int") to str'

#Below is the way how we concatenate two different data types

print("{} {}".format("Value is: ", b))

#To know what kind of Data Type is attached to the variable

print ( type (b) )
print ( type (c) )
print ( type (d) )
