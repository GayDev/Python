class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class linked_list:
    def __init__(self):
        self.root=None

    def is_empty(self):
        if self.root==None:
            return True
        else:
            return False
    
    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(self.root,value)

    def _insert(self,cur_node,value):
        if cur_node.next==None:
            cur_node.next=node(value)
        else:
            self._insert(cur_node.next,value)
    
    def delete(self,value):
        if self.is_empty==True:
            print("List is empty!")
        else:
            self._delete(self.root,value)
        
    def _delete(self,cur_node,value):
        if cur_node.value==value:
            cur_node=cur_node.next
        else:
            self._delete(cur_node.next,value)

    def print(self):
        if self.is_empty==True:
            print("List is empty!")
        self._print(self.root)

    def _print(self,cur_node):
        print(cur_node.value)
        if cur_node.next!=None:
            self._print(cur_node.next)
    

            

a = linked_list()
a.insert(3)
a.print()
a.insert(4)
a.insert(8)
a.insert(20)
a.print()
a.delete(3)
a.print()
