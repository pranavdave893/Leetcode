import heapq
from collections import Counter


def output(elements):
    heap = []
    element_to_frequency = Counter(elements)
    elements = []

    for element, frequency in element_to_frequency.items():
        heapq.heappush(heap, (frequency, -element))

    while heap:
        frequency, element = heapq.heappop(heap)
        elements.extend([-element] * frequency)

    return elements

print (output([7,7,7,7,2,2,3,3,1,1,9,9,9,9,9,6,6,6,6]))