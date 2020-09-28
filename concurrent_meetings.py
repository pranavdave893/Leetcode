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

print (meeting_rooms([(100, 300), (145, 215), (200, 230), (215, 300), (215, 400), (500, 600)]))