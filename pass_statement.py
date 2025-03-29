## pass statement is used as a placeholder for future statements.
## eg. we have a loop that is not yet implemented but we may wish to write some code in it in the future then we can use the pass statement instead of an empty body of the loop.

for i in range(5):
    pass
    print(i, end = " ")
print("Done")
