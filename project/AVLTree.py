import random
from wordreading import inserted

class Node:
    def __init__(self, data):
        self.key = data
        self.height = 1
        self.left = None
        self.right = None
        self.color = 1  # red: 1, black: 0
    


class AVLTree:
    def __init__(self):
        self.root = None

    def search(self,key):
        # print(self.root.key)
        return self._search(self.root,key)

    def _search(self, node, key):
        # print(node.key)
        # print("_search")
        if not node :
            # print("no node error")
            
            return None
        elif node.key == key:
            # print("found")
            return node.key
        elif key < node.key:
            # print("left")
            return self._search(node.left, key)
        else:
            # print("right")
            return self._search(node.right, key)

    # Function to get the height of the tree
    def height(self, node):
        if not node:
            return 0

        return node.height

    # Function to get the balance factor of a node 
    def balance_factor(self, node):
        if not node:
            return 0

        return self.height(node.left) - self.height(node.right)

    # Function to perform a right rotation
    def right_rotate(self, node):
        if node.key == self.root.key:
            self.root = node.left
        left_child = node.left
        right_child = left_child.right

        left_child.right = node
        node.left = right_child

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        left_child.height = 1 + max(self.height(left_child.left), self.height(left_child.right))

        return left_child

    # Function to perform a left rotation
    def left_rotate(self, node):
        if node.key == self.root.key:
            self.root = node.right
        right_child = node.right
        left_child = right_child.left

        right_child.left = node
        node.right = left_child

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        right_child.height = 1 + max(self.height(right_child.left), self.height(right_child.right))

        return right_child

    # Function to insert a node into the tree
    def insert_node(self, node, new_node):
        key = new_node
        if not node:
            if self.root is None:
                self.root = Node(new_node)
            return Node(new_node)
        elif key < node.key:
            node.left = self.insert_node(node.left, new_node)
        else:
            node.right = self.insert_node(node.right, new_node)

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance_factor = self.balance_factor(node)

        # Left-Left case
        if balance_factor > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right-Right case
        if balance_factor < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left-Right case
        if balance_factor > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right-Left case
        if balance_factor < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # Function to delete a node from the tree
    def delete_node(self, node, data):
        key = data
        if not node:
            return node

        elif key < node.key:
            node.left = self.delete_node(node.left, key)

        elif key > node.key:
            node.right = self.delete_node(node.right, key)

        else:
            # Node with only one child or no child
            if not node.left:
                temp = node.right
                node = None
                return temp

            elif not node.right:
                temp = node.left
                node = None
                return temp

            # Node with two children
            temp = self.get_min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete_node(node.right, temp.key)

        if not node:
            return node

        node.height = max(self.height(node.left), self.height(node.right))-1

        balance_factor = self.balance_factor(node)

        # Left-Left case
        if balance_factor > 1 and key > node.left.key:
            return self.right_rotate(node)

        # Right-Right case
        if balance_factor < -1 and key < node.right.key:
            return self.left_rotate(node)

        # Left-Right case
        if balance_factor > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right-Left case
        if balance_factor < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node
    
    # Function to print the tree in-order
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            # print((node.key,node.value), end=' ')
            print(node.key, end=' '  )
            self.in_order_traversal(node.right)
    
    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

# #testing part

# tree = AVLTree()

# list_b = ["raza","hashim","fatima","tariq","hammad","nadeem","tahir","ghazi"]

# for i in list_b:
#     tree.insert_node(tree.root,i)

# tree.in_order_traversal(tree.root)
# print("\n")

# tree.delete_node(tree.root,"raza")

# tree.in_order_traversal(tree.root)

