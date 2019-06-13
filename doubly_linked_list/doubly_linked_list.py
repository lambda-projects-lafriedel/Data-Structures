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
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)

        if current_next: # if not None
            current_next.prev = self.next

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
        if self.head:
            self.head.prev = new_head
        elif not self.head and not self.tail:
            self.tail = new_head
        # set self.head as new_head
        self.head = new_head
        # increase length of DLL by 1
        self.length += 1

    def remove_from_head(self):
        removed_head = self.head
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head:
            new_head = self.head.next
            # set the head as the current head's next
            self.head = new_head
            # set the newly set head's previous as None
            self.head.prev = None
            # return removed_head
        
        # if length of DLL is greater than 0, decrease length by 1
        if self.length > 0:
            self.length -= 1
        
        return removed_head.value
          

    def add_to_tail(self, value):
        # create new ListNode of value, with its prev value as the current tail
        new_tail = ListNode(value, self.tail, None)
        # set current tail's next as new tail
        if self.tail:
            self.tail.next = new_tail
        elif not self.tail and not self.head:
            self.head = new_tail
        # set self.tail as new tail
        self.tail = new_tail
        # increase length of DLL by 1
        self.length += 1

    def remove_from_tail(self):
        removed_tail = self.tail

        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.tail is not None:
            new_tail = self.tail.prev
            # set the tail's prev as the new tail
            self.tail = new_tail
            # set the new tail's next to None
            self.tail.next = None
        
        # if DLL's length is greater than 0, decrease length by 1
        if self.length > 0:
            self.length -= 1

        # return removed_tail
        return removed_tail.value

    def move_to_front(self, node):
        value = node.value

        if node is self.head:
            return
    
        if node is self.tail:
            self.remove_from_tail()
            self.add_to_head(value)
        else:
            self.delete(node)
            self.add_to_head(value)

    def move_to_end(self, node):
        value = node.value
        # Return if already trying to move the tail to the end
        if node is self.tail:
            return

        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            self.delete(node)
            self.add_to_tail(value)

    def delete(self, node):

        if node is self.tail:
            self.remove_from_tail()
        elif node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            if self.length > 0:
                self.length -= 1
      
    def get_max(self):
        # if self.head is self.tail return self.head.value
        if self.head is self.tail:
            return self.head.value

        # store highest value in a variable
        highest_value = self.head.value
        # store self.head in a variable
        current = self.head.next
        # while there's a next attribute that's not None, loop through and compare values
        while current:
        # if the value of each node is higher than the value stored in variable, change the variable
            if current.value > current.prev.value:
                highest_value = current.value
            current = current.next
        
        # return the variable
        return highest_value
