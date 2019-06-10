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
          
        added_node = Node(item) # new_node.value = 5
                              # new_node.next = none
        if not self.tail:
            self.head = added_node
            self.tail = added_node
        else:
            self.tail.next = added_node # next = 5
            self.tail = self.tail.next # tail = 5
    
    def remove_from_front(self):
        if self.head:
            removed_node = self.head
            self.head = self.head.next
            return removed_node.value
        else:
            return "Cannot dequeue, queue is empty"

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_back(item)
    self.size += 1
  
  def dequeue(self):
    self.storage.remove_from_front()
    self.size -= 1

  def len(self):
    return self.size
