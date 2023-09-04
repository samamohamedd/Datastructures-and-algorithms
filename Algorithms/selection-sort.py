def find_smallest (arr):
    smallest = arr[0]
    index = 0
    for i in range (1, len(arr)) :
        if arr[i] < smallest:
            smallest = arr[i]
            index = i
    return index

def sort_array(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr 

a = [4,22,66,3,45,62,55,6,10,2,]
print(sort_array(a))