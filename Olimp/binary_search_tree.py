class node:
    def __init__(value):
        self.value=value
        self.left_child=None
        self.right_child=None

class binary_search_tree:
    def __init__():
        self.root=None
    
    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            _insert(self.root,value)

    def _insert(self,cur_node,value):
        if value < cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child=node(value)
            else:
                _insert(cur_node.left_child, value)
        elif value > cur_node.value
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
            else:
                _insert(cur_node.right_child, value)
    
    def _print(self,cur_node):
        if cur_node.left_child!=None:
            _print(cur_node.left_child)
        print(cur_node.value, end=' ')
        if cur_node.right_child!=None:
            _print(cur_node.right_child)

    
