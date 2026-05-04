# while-loop syntax

num = 4

while num>=1:
    print(num)
    num = num-1

print('While Loop execution completed')


# Now Skipping the value '3' from the output
num1 = 4
while num1>1:
    if num1 != 3:
        print(num1)
    num1 = num1-1

print('Skipping the value \'3\' from the output')


#Using 'break' keyword in while loop

num2 = 4
while num2>1:
    if num2 == 3:
        break
    print(num2)
    num2 = num2-1

print("Break keyword logic execution completed")


#Using 'continue' keyword in while loop

number = 10
while number>1:
    if number == 9:
        number = number - 1
        continue
    if number == 3:
        break
    print(number)
    number = number - 1

print("continue keyword code example completed.")