
lst = [10, 20, 40, 30, 20, 30]

    
def bubble_sort(lst):
    n = len(lst) - 1
    for i in range(0, n):
        for j in range(i, n):
            if lst[j] > lst[j + 1]:
                swap(lst, j, j + 1)   
    return lst
    
def swap(lst, j, k):
    lst[j], lst[k] = lst[k], lst[j]
    
    
print(bubble_sort(lst))
