
class Node:
    def __init__(self,data=None):
        self.data = None
        self.next = None
        self.length = 0
    
    def get_data(self):
        return self.data
    
    def set_data(self,data):
        self.data = data
        
    def get_next(self):
        return self.next
    
    def set_next(self,next):
        self.next = next
    
    def has_next(self):
        return self.next != None
    
    def print_list(self):
        current = self.head
        print "[",
        while current != None:
            print current.data,
            current = current.get_next()
            if not current is None:
                print ",",
        print "]",
    
    def insert_at_beginning(self,data):
        new_node = Node()
        new_node.set_data(data)

        if self.length == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1
    
    def insert_at_end(self,data):
        new_node = Node()
        new_node.set_data(data)

        current = self.head

        while current.get_next() != None:
            current = current.get_next()
        
        current.set_next(new_node)
        self.length += 1
    
    def insert_at_pos(self,data,pos):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insert_at_beginning(data)
            elif pos == self.length:
                self.insert_at_end(data)
            else:
                new_node = Node()
                new_node.set_data(data)
                count = 1
                current = self.head
                while count < pos-1:
                    count += 1
                    current = current.get_next()

                new_node.set_next(current.get_next())
                current.set_next(new_node)
                self.length += 1
    
    def delete_with_node(self,node):
        if self.length == 0:
            raise ValueError("LinkedList is Empty")
        else:
            current = self.head
            previous = None
            found = False
        
        while not found:
            if current == node:
                found = True
            elif current is None:
                raise ValueError("Node not in LinkedList")
            else:
                previous = current
                current = current.get_next()
        
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        
        self.length -= 1
    
    def delete_value(self,value):
        current = self.head
        previous = current

        while current != None or current.data == value:
            if current.data == value:
                previous.next = current.next 
                self.length -= 1
                return
            else:
                previous = current
                current = current.next
        raise ValueError("Node not in the List.")
    
    def delete_at_position(self,pos):
        count = 0
        current = self.head
        previous = self.head

        if pos > self.length or pos < 0:
            raise ValueError("Position Does not exist.")
        
        if pos == 0:
            self.head = current.next
            return
        
        while current != None:
            if count == pos:
                previous.next = current.next
                self.length -= 1
                return
            else:
                previous = current
                current = current.next
                count += 1
    def clear():
        self.head = None

    # Print linked List backwards with recursion
    # def print_backward(list):
    #     if list == None: return
    #     head = list
    #     tail = list.next
    #     print_backward(tail)
    #     print head,


node = Node()
node.insert_at_beginning(1)
node.insert_at_end(2)
node.insert_at_end(3)
node.print_list()

# node.set_next(node2)
# node2.set_next(node3)




node 


    




