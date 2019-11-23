class node:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(self.root,value)

    def _insert(self,cur_node,value):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
            else:
                self._insert(cur_node.left_child, value)
        if value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
            else:
                self._insert(cur_node.right_child, value)
            
    