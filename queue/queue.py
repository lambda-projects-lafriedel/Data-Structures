class Node:
    def __init__(self, value, next):
        self.value = value # 3 ==>    3, 5
        self.next = next   # None ==> 5, none

class LinkedList:
    def __init__(self):
        self.head = None # 3
        self.tail = None # 3
                          # 5
    def add_to_back(self, item):
          
        new_node = Node(item) # new_node.value = 5
                              # new_node.next = none
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # next = 5
            self.tail = self.tail.next # tail = 5
    
    def remove_from_front(self):
        if self.head:
            removed_node = self.head
            self.head = self.head.next
            return removed_node.value
    
    def get_length(self):
        pass

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_back(item)
  
  def dequeue(self):
    self.storage.remove_from_front()

  def len(self):
    pass
