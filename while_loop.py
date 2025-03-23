# to print first 10 numbers using while loop :
def print_10():
    i = 0 
    while i <= 10:
        print(i, end = " ")
        i = i + 1
print_10()


# write a program to calculate the sum and average of first 10 numbers.

i = 0
sum = 0
while i <= 10:
    sum = sum + i 
    i += 1
avg = sum/10

print("the sum is ", sum)
print("the average is", avg)
