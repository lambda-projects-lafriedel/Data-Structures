class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
      # check if value is less than our current node's value
      if value < self.value:
          # if there's no left child, place new node here, else perform insert again
          if not self.left:
              self.left = BinarySearchTree(value)
          else:
              self.left.insert(value)
      # elif value is greater than/equal to current node value
      elif value >= self.value:
          # if there's no right child, place new node here, else perform insert again
          if not self.right:
              self.right = BinarySearchTree(value)
          else:
              self.right.insert(value)

  def contains(self, target):
      # if target = self.value, return True
      if target == self.value:
          return True
      # if target is less than self.value,
      elif target < self.value:
          # if not self.left:
          if not self.left:
              # return False
              return False
          # else continue search in left subtree
          else:
              return self.left.contains(target)
      # if target is greater than self.value,
      elif target > self.value:
          # if not self.right:
          if not self.right:
              # return False
              return False
          # else continue search in right subtree
          else:
              return self.right.contains(target)

  def get_max(self):
      # if self.right and self.left == None, return self.value
      if not self.right and not self.left:
          return self.value
      # store current node in a variable
      node = self
      # while there's a right node (meaning a larger value), traverse down the tree into self.right
      while node.right is not None:
          node = node.right

      # when there's no longer a self.right, return self.value
      return node.value

  def for_each(self, cb):
    # if self.right call for_each on self.right
    if self.right:
        self.right.for_each(cb)
    # if self.left call for_each on self.left
    if self.left:
        self.left.for_each(cb)

    return cb(self.value)