import heapq

list1 = [1,5,9,2,4,6,8]

heap1 = []

k = 4
c = 0

for i in range(len(list1)):

    if c < k:
        heapq.heappush(heap1,list1[i])
        c += 1
    else:
        root = heapq.heappop(heap1)

        if root < list1[i]:
            heapq.heappush(heap1,list1[i])
        
        else:
            heapq.heappush(heap1,root)

print(heapq.heappop(heap1))
