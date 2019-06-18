class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # append value to the end of the list
    self.storage.append(value)
    # utilize bubble_up
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    # store ref to first element, to be returned
    if self.get_size() > 0:
        max_elem = self.storage.pop(0)
        #move last num in array to first index and pop the last value off
        if self.get_size() > 0:
            last_elem = self.storage.pop()
            self.storage.insert(0, last_elem)
            # call sift_down
            self._sift_down(0)
        return max_elem

  def get_max(self):
    # return first element
    return self.storage[0]

  def get_size(self):
    # return length of self.storage
    return len(self.storage)

  def _bubble_up(self, index):
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
      # while index is less than the length of self.storage
      while index < len(self.storage):
          print("IDX:", index)
      # get the left and right child indices
          l_index = 2 * index + 1
          r_index = 2 * index + 2 if l_index + 1 < len(self.storage) else l_index
          print("L AND R:", l_index, r_index)
          if l_index < len(self.storage) and r_index < len(self.storage):
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
          else:
              break
