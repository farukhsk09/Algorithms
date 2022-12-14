from functools import reduce
from heapq import heapify, heappush, heappop

# Creating empty heap
heap = []
heapify(heap)

heappush(heap, 400)
heappop(heap)

myList=[10,3,14,15,44,8]
maxValue = reduce((lambda x,y : x if x>y else y),myList)
doubled = list(map((lambda x :  x*2),myList))
print(maxValue)
print(doubled)