import heapq

def meeting_rooms(meetings):
    meetings.sort(key=lambda x:x[0])  # sort by start time
    heap = [meetings[0][1]]  # heap contains end times only
    max_len, max_start, max_end = 0, 0, 0
    for meeting in meetings[1:]:
        
        while heap and meeting[0] >= heap[0]:
            heapq.heappop(heap)  # pop all meetings that end before current meeting
        heapq.heappush(heap, meeting[1])
        
        if len(heap) > max_len:
            max_len = len(heap)
            max_start = meeting[0]
            max_end = heap[0]
    print(max_start, max_end)


def meeting_rooms_2(meetings):
    from functools import reduce

    max_time = reduce(lambda x, y: x if x > y else y, meetings)[1]
    
    times = [0] * max_time

    for x, y in meetings:
        for i in range(x, y):
            times[i] += 1

    max_value = max(times)

    def first_occurence(a):
        for i, x  in enumerate(a):
            if x == max_value:
                return i
    
    left = first_occurence(times)
    right = max_time - first_occurence(times[::-1])

    return (left, right)



print (meeting_rooms_2([(100, 300), (145, 215), (200, 230), (215, 300), (215, 400), (500, 600)]))