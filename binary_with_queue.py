from queue import Queue

q = Queue()
n = int(input())
q.put("1")

while(n):
	n -= 1

	s1 = q.get()

	print (s1)

	s2 = s1

	q.put(s1+"0")

	q.put(s2+"1")

