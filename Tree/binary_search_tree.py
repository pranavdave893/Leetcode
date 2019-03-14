import Queue
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    
    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)

        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)
    
    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)
        
        return value == self.value
    
    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None
    
    def find_minimum_value(self):
        if self.left_child:
            return self.left_child.find_minimum_value()
        else:
            return self.value
    
    def bfs(self):
        queue = Queue.Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print current_node.value

            if current_node.left_child:
                queue.put(current_node.left_child)
            
            if current_node.right_child:
                queue.put(current_node.right_child)
    
    def remove_node(self, value, parent):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)

            return True
    
    def zigzagtraversal(self):
        if self is None:
            return
        
        currentlevel = []
        nextlevel = []

        ltr = False
        currentlevel.append(self)
        result = [[self.value]]
        while currentlevel:
            temp = currentlevel.pop(-1)
            print (temp.value)
            
            if ltr:
                if temp.left_child:
                    nextlevel.append(temp.left_child)
                if temp.right_child:
                    nextlevel.append(temp.right_child)
            else:
                if temp.right_child:
                    nextlevel.append(temp.right_child)
                if temp.left_child:
                    nextlevel.append(temp.left_child)
            
            if not currentlevel:
                ltr = not ltr
                # print nextlevel
                temp_res = []
                for node in nextlevel:
                    temp_res.append(node.value)
                if temp_res:
                    result.append(temp_res)
                currentlevel, nextlevel = nextlevel, currentlevel
        
        # print result

bst = BinarySearchTree(3)
bst.insert_node()
bst.insert_node(20)
bst.insert_node(15)
bst.insert_node(7)
# bst.insert_node(17)
# bst.insert_node(25)
# bst.insert_node(19)
# bst.bfs()
# bst.remove_node(20,None)

# bst.bfs()
bst.zigzagtraversal()