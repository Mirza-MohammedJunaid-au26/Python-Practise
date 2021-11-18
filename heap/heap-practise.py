import heapq

arr = [4,5,8,9,1,2,3,6,7]
heapq.heapify(arr)
print(arr)
heapq.heappushpop(arr,10)
print(arr)
print(heapq.heapreplace(arr,11))
print(arr)
heapq._heapify_max(arr)
print(arr)
print(heapq._heappop_max(arr))
print(arr)
