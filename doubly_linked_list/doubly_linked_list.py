"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value # 2
    self.prev = prev # 1
    self.next = next # 3

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is pointing to."""
  def insert_after(self, value): # 4
    current_next = self.next # 3
    self.next = ListNode(value, self, current_next)
    # 3 is now 4, and 4's next is now 3, so LL is 1, 2, 4, 3
    if current_next: # if not None
      current_next.prev = self.next # 3's prev is now 4 -- have to do this for the DLL

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    # create new ListNode of value, with no prev value and its next value as the current head
    new_head = ListNode(value, None, self.head)
    # set current head's prev as new_head
    if self.head is not None:
        self.head.prev = new_head
    # set self.head as new_head
    self.head = new_head

  def remove_from_head(self):
    pass

  def add_to_tail(self, value):
    pass

  def remove_from_tail(self):
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass
