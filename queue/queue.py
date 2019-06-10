class Node:
    def __init__(self, value, next):
        self.value = value # 3 ==>    3, 5
        self.next = next   # None ==> 5, none
    
    def change_next(self, new_next)
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None # 3
        self.tail = None # 3
                          # 5
    def add_to_back(self, item):
          
        new_node = Node(item) # new_node.value = 5
                              # new_node.next = none
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # next = 5
            self.tail = self.tail.next # tail = 5
    
    def remove_from_front(self):
        pass
    
    def get_length(self):
        pass

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    pass
  
  def dequeue(self):
    pass

  def len(self):
    pass
