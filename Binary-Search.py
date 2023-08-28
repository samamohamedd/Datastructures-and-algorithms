def Binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return False


l = [2, 4, 5, 6, 9]
print(Binary_search(l, 4))
print(Binary_search(l, 10))
