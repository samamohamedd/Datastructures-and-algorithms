def bubbles(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


l = [4, 2, 3, 10, 1, 5, 3, 7, 9]
print(bubbles(l))

# ===================================================================


def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = int(len(arr) / 2)
    left = [x for x in arr[:mid]]
    right = [x for x in arr[mid:n]]
    return helper(merge_sort(left), merge_sort(right))


def helper(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr


l = [4, 2, 3, 10, 1, 5, 3, 7, 9]
print(merge_sort(l))
