class Node:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left, self.right = None, None

class MyCalendar(object):
    def __init__(self):
        self.root = None
    

    def book_helper(self, root, start, end):
        if start >= root.end:
            if root.right:
                return self.book_helper(root.right, start, end)
            root.right = Node(start, end)
            return True
        
        elif end <= root.left:
            if root.left:
                return self.book_helper(root.left, start, end)
            root.left = Node(start, end)
            return True
        
        else:
            return False
    

    def book(self, start, end) -> bool:

        if not self.root:
            self.root = Node(start, end)
            return True
        return self.book_helper(self.root, start, end)