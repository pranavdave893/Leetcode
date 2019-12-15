# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root:
            head, tail = self.helper(root)
            return head
        return None
    
    def helper(self, root):
        head, tail = root, root
        if root.left:
            lh, lt = self.helper(root.left)
            lt.right = root
            root.left = lt
            head = lh
        if root.right:
            rh, rt = self.helper(root.right)
            rh.left = root
            root.right = rh
            tail = rt
        
        head.left = tail
        tail.right = head

        return(head, tail)


        # self.head = None
        # self.tail = None

        # if not root.left and not root.right:
        #     root.left = root
        #     root.right = root
        #     return root

        # def joinNodes(main_root, root, is_right):
        #     if not root:
        #         return

        #     left_node = joinNodes(main_root, root.left, False)
        #     right_node = joinNodes(main_root, root.right, True)

        #     if not left_node and not right_node: 
        #         if not is_right:
        #             self.head = root
        #         else:
        #             self.tail = root
        #         return root
            
        #     if left_node:
        #         left_node.right = root
        #         root.left = left_node
            
        #     if right_node:
        #         right_node.left = root

        #     if root == main_root:
        #         if right_node:
                    
        #             if self.tail and not self.head:
        #                 self.head = root
                    
        #             self.tail.right = self.head
        #             self.head.left = self.tail
        #         else:
        #             root.right = self.head
        #             self.head.left = root
        #         return self.head

        #     elif left_node and right_node:
        #         return right_node
        #     else:
        #         return root
        
        # return joinNodes(root, root, False)


node = Node(1, None, Node(2, None, None))
abc = Solution()
print (abc.treeToDoublyList(node))