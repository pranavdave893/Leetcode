class Solution():
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        res = []

        def delete_node(root, is_parent=False):
            if not root:
                return None
            
            if root.val in to_delete:
                root.left = delete_node(root.left)
                root.right = delete_node(root.right)
                return None
            
            else:
                if not is_parent:
                    res.append(root)    
                
                root.left = delete_node(root.left, True)
                root.right = delete_node(root.right, True)

                return root
        
        delete_node(root)

        return res