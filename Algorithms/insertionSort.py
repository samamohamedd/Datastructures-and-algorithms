def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i] #current element
        j = i-1 # index of the previous element

        # shifting elements that are greater than our current one position ahead
        while j >= 0 and arr[j] > current:
            arr[j+1] = arr[j] #shifting to the right 
            j -= 1

        arr[j+1] = current #putting the current in its right position

    return arr    


l = [4, 2, 9, 6, 10,5]
print(insertion_sort(l))
