class Node(object):
    def __init__(self,data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        self.length = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        return repr(self.data)
    
    def print_list(self):
        current = self.head
        print "[",
        while current != None:
            print current.data,
            current = current.next
            if not current is None:
                print ",",
        print "]",
    
    def insert_at_beginning(self,data):
        new_node = Node(data,None,None)
        
        if(self.length == 0):
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None
            self.head = new_node
        self.length += 1

    def insert_at_end(self,data):
        new_node = Node(data,None,None)
        

        if(self.head == None):
            self.head = new_node
            self.tail = new_node
            self.prev = new_node
            self.next = new_node
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
        self.length +=1
    
    def get_node(self,index):
        current = self.head
        if current  == None:
            return None
        i = 0
        while i<index and current.next != None:
            current = current.next
            if current == None:
                break
            i += 1
        return current

            
    def insert_at_middle(self,data,index):
        new_node = Node(data,None,None)

        if index == 0:
            self.insert_at_beginning(data)
        
        elif index>0:
            temp = self.get_node(index)

            if temp == None or temp.next == None:
                self.insert_at_end(data)
            else:
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node
            self.length +=1
    
    def delete_from_beginning(self):
        self.head = self.head.next
        if self.head:
            self.head.prev = None
            self.length -= 1

    
    def delete_with_index(self,index):
        if index == 0:
            self.delete_from_beginning()
        elif index<self.length:
            temp = self.get_node(index)
            temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev
            temp.prev = None
            temp.next = None
            temp.data = None
        else:
            raise ValueError("Index out of Bound.")
    
    def delete_with_data(self,data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                if temp == self.head:
                    self.delete_from_beginning()
                    break
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                    temp.prev = None
                    temp.next = None
                    temp.data = None
            temp = temp.next
                 


# node = Node()
# # node.insert_at_beginning(4)
# node.insert_at_end(5)
# node.insert_at_end(6)
# node.insert_at_end(7)
# node.insert_at_beginning(10)
# node.insert_at_middle(10,3)
# node.delete_with_data(10)
# node.delete_with_data(10)
# node.delete_with_data(5)
# node.delete_with_data(6)
# node.delete_with_data(4)
# node.print_list()