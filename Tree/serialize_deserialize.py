from create_tree import BinarySearchTree
root = BinarySearchTree(1)
left = bs.insert_left(2)
right = bs.insert_right(3)
left.insert_right(5)
right.insert_right(4)

class Codec:
    def serialize(self, root):
        def doit(node): 
            if node:
                doit(node.left)
                doit(node.right)
                val.append(node.val)
            else:
                val.append('#')

        val = []
        doit(root)
        return val
    
    # def deserialize(self, data):
            
            
        

    #     return doit(data, 0)

                

                        



codec = Codec()
ser = code.serialize(root)
print ser
# code.deserialize(code.serialize(root))