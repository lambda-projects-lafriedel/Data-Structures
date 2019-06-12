class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    pass
    # if inserted value is larger than the root, place it as new root

  def delete(self):
    pass
    # if root, next highest number needs to bubble up to root
    # store ref to first element, and move last num in array to first index and pop the last value off
    # check max spot's two children using formulas, and if either or both values are higher than the parent, swap the highest num with old max spot
    # keep checking until neither child node is equal or greater than OR it has no children

  def get_max(self):
    pass
    # return first element

  def get_size(self):
    pass

  def _bubble_up(self, index):
      # keep bubbling up until the top of the heap is reached, or the parent is higher priority
      while index > 0:
          # while index is > 0, get parent index and compare
          p_index = (index - 1) // 2
          # if curr index is greater than parent, swap
          if self.storage[index] > self.storage[p_index]:
              self.storage[index], self.storage[p_index] = self.storage[p_index], self.storage[index]
              # set index as parent index, since that's where the item at the original index now is
              index = p_index
          else:
              break

  def _sift_down(self, index):
      # keep sifting down until the bottom of the heap is reached, or the child is a lower priority
      # while index is less than the length of self.storage
      while index < len(self.storage):
      # get the left and right child indices
          l_index = 2 * index + 1
          r_index = 2 * index + 2
          # if l and r indices are equal, swap with right index
          if self.storage[l_index] == self.storage[r_index]:
              self.storage[index], self.storage[r_index] = self.storage[r_index], self.storage[index]
              # set index as the right index, since that's index's new loc
              index = r_index
          # if curr index is less than either or both of its children
          elif self.storage[index] < self.storage[l_index] or self.storage[index] < self.storage[r_index]:
              # if right index is greater than left index, swap right index and curr index
              if self.storage[r_index] > self.storage[l_index]:
                   self.storage[index], self.storage[r_index] = self.storage[r_index], self.storage[index]
                   # set index as right index, since that's index's new loc
                   index = r_index
              # else swap left index and curr index
              else:
                   self.storage[index], self.storage[l_index] = self.storage[l_index], self.storage[index]
                   # set index as left index, since that's index's new loc
                   index = l_index
          else:
            break

      # set index as value of the index it was switched to, since that's its new location
