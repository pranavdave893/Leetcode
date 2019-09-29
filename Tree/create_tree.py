class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = (value)
            new_node.left_child = self.left_child
            self.left_child = new_node
    
    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def pre_order(self, value):
        print self.value

        if self.left_child:
            self.left_child.pre_order()
        
        if self.right_child:
            self.right_child.pre_order()
    
    def in_order(self, value):
        if self.lef_child:
            self.left_child.in_order()
        
        print self.value

        if self.right_child:
            self.right_child.in_order()
    
    def post_order(self, value):
        if self.left_child:
            self.left_child.post_order()
        
        if self.right_child:
            self.right_child.post_order()
        
        print self.value
    
    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print current_node.value

            if current_node.lef_child:
                queue.put(current_node.lef_child)
            
            if current_node.right_child:
                queue.put(current_node.right_child)

    def zigzagtraversal(self):
        if self is None:
            return
        
        currentlevel = []
        nextlevel = []

        ltr = True
        currentlevel.append(self)
        
        while currentlevel:
            temp = currentlevel.pop(-1)
            # print (temp.value, " ", end="")
            
            if ltr:
                if temp.left_child:
                    currentlevel.append(temp.left_child)
                if temp.right_child:
                    currentlevel.append(temp.right_child)
            else:
                if temp.right_child:
                    currentlevel.append(temp.right_child)
                if temp.left_child:
                    currentlevel.append(temp.left_child)
            
            if not currentlevel:
                ltr = not ltr
                currentlevel, nextlevel = nextlevel, currentlevel


bs = BinarySearchTree(1)
left = bs.insert_left(2)
right = bs.insert_right(3)
left.insert_right(5)
right.insert_right(4)