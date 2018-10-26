import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

heap = []
print('Random: ',data)
print()

for n in data:
    print('add {:>3}'.format(n))
    heapq.heappush(heap,n)
    show_tree(heap)
