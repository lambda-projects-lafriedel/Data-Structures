class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_back(self, item):
          
        added_node = Node(item)

        if not self.tail and not self.head:
            self.head = added_node
            self.tail = added_node
        else:
            self.tail.next = added_node
            self.tail = added_node
    
    def remove_from_front(self):
        if not self.head and not self.tail:
            return None

        if self.head is self.tail:
            front_node = self.head
            self.head = None
            self.tail = None
            return front_node.value

        front_node = self.head
        self.head = front_node.next
        return front_node.value


class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_back(item)
    self.size += 1
  
  def dequeue(self):
    if self.size > 0:
        self.size -= 1

    return self.storage.remove_from_front()

  def len(self):
      return self.size
