
# # Create a node
# class BTreeNode:
#   def __init__(self, leaf=False):
#     self.leaf = leaf
#     self.keys = []
#     self.children = []


# # Tree
# class BTree:
#   def __init__(self, t):
#     self.root = BTreeNode(True)
#     self.t = t

#     # Insert node
#   def insert(self, k):
#     root = self.root
#     if len(root.keys) == (2 * self.t) - 1:
#       temp = BTreeNode()
#       self.root = temp
#       temp.children.insert(0, root)
#       self.split_child(temp, 0)
#       self.insert_non_full(temp, k)
#     else:
#       self.insert_non_full(root, k)

#     # Insert nonfull
#   def insert_non_full(self, x, k):
#     i = len(x.keys) - 1
#     if x.leaf:
#       x.keys.append((None, None))
#       while i >= 0 and k[0] < x.keys[i][0]:
#         x.keys[i + 1] = x.keys[i]
#         i -= 1
#       x.keys[i + 1] = k
#     else:
#       while i >= 0 and k[0] < x.keys[i][0]:
#         i -= 1
#       i += 1
#       if len(x.children[i].keys) == (2 * self.t) - 1:
#         self.split_child(x, i)
#         if k[0] > x.keys[i][0]:
#           i += 1
#       self.insert_non_full(x.children[i], k)

#     # Split the child
#   def split_child(self, x, i):
#     t = self.t
#     y = x.children[i]
#     z = BTreeNode(y.leaf)
#     x.children.insert(i + 1, z)
#     x.keys.insert(i, y.keys[t - 1])
#     z.keys = y.keys[t: (2 * t) - 1]
#     y.keys = y.keys[0: t - 1]
#     if not y.leaf:
#       z.children = y.children[t: 2 * t]
#       y.children = y.children[0: t - 1]

#   # Print the tree
#   def print_tree(self, x, l=0):
#     print("Level ", l, " ", len(x.keys), end=":")
#     for i in x.keys:
#       print(i, end=" ")
#     print()
#     l += 1
#     if len(x.children) > 0:
#       for i in x.children:
#         self.print_tree(i, l)

#   # Search key in the tree
#   def search_key(self, k, x=None):
#     print(k)
#     if x is not None:
#       i = 0
#       while i < len(x.keys) and k > x.keys[i][0]:
#         i += 1
#       if i < len(x.keys) and k == x.keys[i][0]:
#         return (x, i)
#       elif x.leaf:
#         return None
#       else:
#         return self.search_key(k, x.children[i])
      
#     else:
#       return self.search_key(k, self.root)
    

# from __future__ import (nested_scopes, generators, division, absolute_import, with_statement,
#                         print_function, unicode_literals)


class BTree(object):
  """A BTree implementation with search and insert functions. Capable of any order t."""

  class Node(object):
    """A simple B-Tree Node."""

    def __init__(self, t):
      self.keys = []
      self.children = []
      self.leaf = True
      # t is the order of the parent B-Tree. Nodes need this value to define max size and splitting.
      self._t = t

    def split(self, parent, payload):
      """Split a node and reassign keys/children."""
      new_node = self.__class__(self._t)

      mid_point = self.size//2
      split_value = self.keys[mid_point]
      parent.add_key(split_value)

      # Add keys and children to appropriate nodes
      new_node.children = self.children[mid_point + 1:]
      self.children = self.children[:mid_point + 1]
      new_node.keys = self.keys[mid_point+1:]
      self.keys = self.keys[:mid_point]

      # If the new_node has children, set it as internal node
      if len(new_node.children) > 0:
        new_node.leaf = False

      parent.children = parent.add_child(new_node)
      if payload < split_value:
        return self
      else:
        return new_node

    @property
    def _is_full(self):
      return self.size == 2 * self._t - 1

    @property
    def size(self):
      return len(self.keys)

    def add_key(self, value):
      """Add a key to a node. The node will have room for the key by definition."""
      self.keys.append(value)
      self.keys.sort()

    def add_child(self, new_node):
      """
      Add a child to a node. This will sort the node's children, allowing for children
      to be ordered even after middle nodes are split.
      returns: an order list of child nodes
      """
      i = len(self.children) - 1
      while i >= 0 and self.children[i].keys[0] > new_node.keys[0]:
        i -= 1
      return self.children[:i + 1]+ [new_node] + self.children[i + 1:]


  def __init__(self, t):
    """
    Create the B-tree. t is the order of the tree. Tree has no keys when created.
    This implementation allows duplicate key values, although that hasn't been checked
    strenuously.
    """
    self._t = t
    if self._t <= 1:
      raise ValueError("B-Tree must have a degree of 2 or more.")
    self.root = self.Node(t)

  def insert(self, payload):
    """Insert a new key of value payload into the B-Tree."""
    node = self.root
    # Root is handled explicitly since it requires creating 2 new nodes instead of the usual one.
    if node._is_full:
      new_root = self.Node(self._t)
      new_root.children.append(self.root)
      new_root.leaf = False
      # node is being set to the node containing the ranges we want for payload insertion.
      node = node.split(new_root, payload)
      self.root = new_root
    while not node.leaf:
      i = node.size - 1
      while i > 0 and payload < node.keys[i] :
        i -= 1
      if payload > node.keys[i]:
        i += 1

      next = node.children[i]
      if next._is_full:
        node = next.split(node, payload)
      else:
        node = next
    # Since we split all full nodes on the way down, we can simply insert the payload in the leaf.
    node.add_key(payload)

  def search(self, value, node=None):
    """Return True if the B-Tree contains a key that matches the value."""
    # print(value)
    if node is None:
      node = self.root
    if value in node.keys:
      return True
    elif node.leaf:
      # If we are in a leaf, there is no more to check.
      return False
    else:
      i = 0
      while i < node.size and value > node.keys[i]:
        i += 1
      return self.search(value, node.children[i])

  def print_order(self):
    """Print an level-order representation."""
    this_level = [self.root]
    while this_level:
      next_level = []
      output = ""
      for node in this_level:
        if node.children:
          next_level.extend(node.children)
        output += str(node.keys) + " "
      print(output)
      this_level = next_level


  def delete_key(self, node, key):
    """
    Delete a key from the B-Tree. This method will delete a given key from a given node.
    If the key is not found, it will do nothing.
    """
    i = 0
    while i < node.size and key > node.keys[i]:
        i += 1
    if i < node.size and node.keys[i] == key:
        if node.leaf:
            # The node is a leaf node, simply delete the key.
            node.keys.pop(i)
        else:
            # The node is an internal node. Replace the key with its inorder predecessor or successor, and then delete it.
            if len(node.children[i].keys) >= self._t:
                predecessor = self.get_inorder_predecessor(node.children[i])
                node.keys[i] = predecessor
                self.delete_key(node.children[i], predecessor)
            elif len(node.children[i+1].keys) >= self._t:
                successor = self.get_inorder_successor(node.children[i])
                
                node.keys[i] = successor
                print("successor is ",successor)
                self.delete_key(node.children[i+1], successor)
            else:
                self.merge_nodes(node, i)

    elif not node.leaf:
        # If the key is not found in the current node and the current node is not a leaf, 
        # then it must be in one of the child nodes.
        if len(node.children[i].keys) < self._t:
            self.borrow_from_left_sibling(node, i)
        if len(node.children[i].keys) < self._t and i < node.size and len(node.children[i+1].keys) < self._t:
            self.merge_nodes(node, i)
        elif i == node.size:
            self.delete_key(node.children[i-1], key)
        else:
            self.delete_key(node.children[i], key)
  
  def delete(self, key):
    """
    Delete a key from the B-Tree. This method will delete a given key from the B-Tree.
    If the key is not found, it will do nothing.
    """
    print("root is ",self.root.keys)
    self.delete_key(self.root, key)
    if len(self.root.keys) == 0:
        # The root node is empty. Make its first child the new root.
        self.root = self.root.children[0]

  def delete_internal_node(self, node, i):
    """
    Delete an internal node from the B-Tree. This method will replace the node with its inorder 
    predecessor or successor, and then delete the predecessor or successor.
    """
    if len(node.children[i].keys) >= self._t:
        predecessor = self.get_inorder_predecessor(node.children[i])
        node.keys[i] = predecessor
        self.delete_key(node.children[i], predecessor)
    elif len(node.children[i+1].keys) >= self._t:
        successor = self.get_inorder_successor(node.children[i+1])
        node.keys[i] = successor
        self.delete_key(node.children[i+1], successor)
    else:
        self.merge_nodes(node, i)

  def get_inorder_predecessor(self, key):
    """
    Returns the inorder predecessor of the given key in the B-Tree.
    """
    node = self.search(key)
    if not node:
      return None

    index = node.keys.index(key)
    if index > 0:
      node = node.children[index]
      while not node.leaf:
        node = node.children[-1]
      return node.keys[-1]

    current_node = node
    parent_node = node.parent
    while parent_node and current_node == parent_node.children[0]:
      current_node = parent_node
      parent_node = parent_node.parent
    if not parent_node:
      return None
    return parent_node.keys[parent_node.children.index(current_node) - 1]

  def get_inorder_successor(self, key):
    """
    Returns the inorder successor of the given key in the B-Tree.
    """
    node = self.search(key)
    if not node:
      return None

    index = node.keys.index(key)
    if index < node.size - 1:
      node = node.children[index + 1]
      while not node.leaf:
        node = node.children[0]
      return node.keys[0]

    current_node = node
    parent_node = node.parent
    while parent_node and current_node == parent_node.children[-1]:
      current_node = parent_node
      parent_node = parent_node.parent
    if not parent_node:
      return None
    return parent_node.keys[parent_node.children.index(current_node) + 1]
  
  def merge_nodes(self, parent, left_child, right_child):
        left_child.keys.append(parent.keys.pop(0))
        left_child.keys += right_child.keys
        left_child.children += right_child.children
        parent.children.remove(right_child)

  def borrow_from_left_sibling(self, parent, left_child, child_idx):
      child = parent.children[child_idx]
      child.keys = [parent.keys[child_idx - 1]] + child.keys
      parent.keys[child_idx - 1] = left_child.keys.pop(-1)
      if not child.leaf:
          child.children = [left_child.children.pop(-1)] + child.children

  def borrow_from_right_sibling(self, parent, right_child, child_idx):
      child = parent.children[child_idx]
      child.keys.append(parent.keys[child_idx])
      parent.keys[child_idx] = right_child.keys.pop(0)
      if not child.leaf:
          child.children.append(right_child.children.pop(0))

  def inorder_traversal(self):
        return self._inorder_traversal(self.root)

  def _inorder_traversal(self, node):
      if node is not None:
          results = []
          i = 0
          while i < len(node.keys):
              if not node.leaf:
                  results.extend(self._inorder_traversal(node.children[i]))
              results.append(node.keys[i])
              i += 1
          if not node.leaf:
              results.extend(self._inorder_traversal(node.children[-1]))
          return results

# def main():
#   B = BTree(3)

#   for i in range(10):
#     B.insert((i, 2 * i))

#   B.print_tree(B.root)

#   if B.search_key(8) is not None:
#     print("\nFound")
#   else:
#     print("\nNot Found")





# list_a = ['osseter', 'beleaguer', 'frounceless', 'caririan', 'nondeluding', 'jambarts', 'teledus', 'zein', 'protonematoid', 'circumstantiation', 'peribolos', 'misdiagrammed', 'unmetaphysically', 'incalculableness', 'discurre', 'catmalison', 'pyopneumoperitonitis', 'harmalin', 'constrainable', 'philanthropian']
# list_b = ["raza","hashim","fatima","tariq","hammad","nadeem","tahir"]


# fourway = BTree(2)
# for l in list_a:
#     fourway.insert(l)
# for n in list_b:
#     fourway.insert(n)

# print(fourway.inorder_traversal())

# # fourway.search("raza")

# # print("4way tree:")
# # # print(fourway.print_tree(fourway.root))
# # print("\n")

# # # fourway.delete(fourway.root,"raza")

# for n in list_a:
#     fourway.delete(n)
# print("Post deletion:")
# print(fourway.print_tree(fourway.root))
# print("\n")