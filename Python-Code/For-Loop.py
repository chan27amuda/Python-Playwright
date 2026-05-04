#iterate through list and print each and every value using for loop

obj = [2, 3, 5, 7, 9]
print("Printing each and every element in a List")
for i in obj:
    print(i)


#Now iterate through the same above List and print multiples of 2
print("Print multiples of 2 for the above list")
for i in obj:
    print(i*2)


#Sum of first '5' Natural Numbers

summation = 0
print("Print Sum of first '5' Natural Number: ")
for j in range(1, 6): # Here it will iterate till 'j to j-1' (1 to 5)
    summation = summation + j

print(summation)


#Increment the 'j' value with 2 for every iteration
print("Printing the values ranging from 1 to 10 by incrementing with 2")
for j in range(1,10,2):
    print(j)

#If we don't pass the starting index in range, by default it treat it as '0'
print("Printing the Numbers by skipping starting index in the loop")
for j in range(10):
    print(j)