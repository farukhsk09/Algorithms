import queue

q = queue.PriorityQueue()


# Add some items to the queue with different priorities
q.put((10, 'high priority item'))
q.put((5, 'medium priority item'))
q.put((1, 'low priority item'))

# Add an item with a string priority
# q.put(('A', 'item with string priority'))

# Add an item with a floating-point priority
# q.put((3.14, 'item with float priority'))

print(q.get()[0])