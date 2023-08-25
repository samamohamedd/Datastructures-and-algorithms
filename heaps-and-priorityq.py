import heapq

data = [3, 44, 51, 15, 10, 9, 20, 36, 27]
heapq.heapify(data)  # minheap by default

print(data)

heapq.heappop(data)  # pop and heapify
print(data)

heapq.heappush(data, 2)
print(data)

data = [3, 44, 51, 15, 10, 9, 20, 36, 27]
heapq._heapify_max(data)
heapq._heappop_max(data)

print(data)

data2 = [5, 33, 7, 9, 44, 1]
data3 = heapq.merge(data, data2)  # merged and heapified
print(list(data3))
