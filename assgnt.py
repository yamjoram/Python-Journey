#calculate the sum of 5 numbers.[use variable]
from tkinter import E


first_number = 1
second_number = 2
third_number = 8
fourth_number = 5
fifth_number = 10
total_number = first_number + second_number + third_number + fourth_number + fifth_number
print(total_number)
print(type(total_number))


#find the average of 6 numbers(use variables)
first_number = 10
second_number = 4
third_number = 20
fourth_number = 40
fifth_number = 4
sixth_number = 90
total_number = first_number + second_number + third_number + fourth_number + fifth_number + sixth_number
average_number = (total_number / 6)
print(average_number)


print("*********")
#add two numbers, multiply the answer by 5 and divide the answer by 3 and find the answer modulo 7.
x = 10
y = 20
z = x + y  
z *= 5
z /= 3
z %= 7
print(z)
print(type(z))
z = int(z)
print(z)
print(type(z))

print("*********")

#declare two variables and compare the first variable with the second variable and print out the largest one.

x = 10
y = 5
if x < y:
    print("x is greater than y")
    
else:
    print("y is smaller than x")


print("*********")



    # find the smaller number[1, 7, -1]. store each number in  a separate variable.

x = 1
y = 7
z = -1
if x < y and x < z :
    print("x is smallest")
if y < x and y < z:
    print("y is smallest")
if z < x and z < y:
    print("z is smallest")




