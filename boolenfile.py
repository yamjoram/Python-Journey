age = input("Enter age : ")
amount = input("what's the amount : ")
age = int(age)
amount = int(amount)


if age > 18 and amount >= 10000:
    print(" yes, you're eligible to drink")
if age > 18 and amount < 1000:
    print("you don't have sufficient funds")
    
else :
    print("no, you're not eligible")