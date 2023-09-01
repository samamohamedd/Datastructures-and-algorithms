import random
# using recursion to make sum function:
def sum(l):
    if l == []:
        return 0
    return l[0] + sum(l[1:])


print(sum([2, 5, 3, 4]))


# Write a recursive function to count the number of items in a list.
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


print(count([1, 2, 3, 4]))


# Find the maximum number in a list
def max(list):
    if list == []:
        return 0
    if len(list) == 1:
        return list[0]
    if list[1] > list[0]:
        return max(list[1:])
    return list[0]


print(max([1, 4, 7]))

# ===================================================================

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[random.randint(0,len(arr)-1)]
    less = [i for i in arr[0:] if i < pivot]
    equal = [i for i in arr if i == pivot]
    more = [i for i in arr[0:] if i > pivot]

    return quick_sort(less) + equal + quick_sort(more)

l = [6,3,4,8,8,10,2]
print (quick_sort(l))
