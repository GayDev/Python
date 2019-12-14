class node:
    def __init__(self,value):
        self.value = value
        self.right_child = None
        self.left_child = None
        
        
class binary_search_tree:
    def __init__(self):
        self.root=None
        
    def insert(self,v):
        if self.root==None:
            self.root=node(v)
        else:
            self._insert(self.root,v)
    
    def _insert(self,cur_node,v):
        if v < cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child = node(v)
            else:
                self._insert(cur_node.left_child, v)
                
        elif v > cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child = node(v)
            else:
                self._insert(cur_node.right_child, v)