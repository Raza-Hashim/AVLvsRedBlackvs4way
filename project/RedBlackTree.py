class Node:
    def __init__(self, data):
        self.key = data
        self.height = 1
        self.left = None
        self.right = None
        self.color = 1  # red: 1, black: 0

class RedBlackTree:
    def __init__(self):
        self.null_node = Node(None)  # sentinel node
        self.root = self.null_node  # root initialized as null node

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.null_node:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.null_node:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Insert a node with key in the tree
    def insert(self, node):
        new_node = Node(node)
        new_node.parent = None
        new_node.key = node
        new_node.left = self.null_node
        new_node.right = self.null_node
        new_node.color = 1  # set color to red

        # BST insertion
        y = None
        x = self.root
        while x != self.null_node:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y == None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        # Fixing violations of red-black tree properties
        if new_node.parent == None:
            new_node.color = 0
            return
        if new_node.parent.parent == None:
            return

        self._fix_insert(new_node)

    def _fix_insert(self, new_node):
        key = new_node
        while new_node != self.root and new_node.parent.color == 1:
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                if uncle and uncle.color == 1:
                    # case 1: the uncle node is red
                    new_node.parent.color = 0
                    uncle.color = 0
                    new_node.parent.parent.color = 1
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        # case 2: the uncle node is black and new_node is a right child
                        new_node = new_node.parent
                        self._left_rotate(new_node)
                    # case 3: the uncle node is black and new_node is a left child
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    self._right_rotate(new_node.parent.parent)
            else:
                uncle = new_node.parent.parent.left
                if uncle and uncle.color == 1:
                    # case 4: the uncle node is red
                    new_node.parent.color = 0
                    uncle.color = 0
                    new_node.parent.parent.color = 1
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        # case 5: the uncle node is black and new_node is a left child
                        new_node = new_node.parent
                        self._right_rotate(new_node)
                    # case 6: the uncle node is black and new_node is a right child
                    new_node.parent.color = 0
                    new_node.parent.parent.color = 1
                    self._left_rotate(new_node.parent.parent)
        self.root.color = 0

    def inorder(self):
        self._inorder_helper(self.root)

    def _inorder_helper(self, node):
        if node != self.null_node:
            self._inorder_helper(node.left)
            print(node.key, end=" ")
            self._inorder_helper(node.right)

    def find(self, key):
        return self._find(key, self.root)
    
    def _find(self, key, node):
        if node is None:
            return None
        elif node.key == key:
            return node.key
        elif key < node.key:
            return self._find(key, node.left)
        else:
            return self._find(key, node.right)
        
    def delete(self, key):
        z = self._del_find(key, self.root)
        if z == None:
            print("Node not found!")
            return

        y = z
        y_original_color = y.color
        if z.left == self.null_node:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.null_node:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 0:
            self._fix_delete(x)

    def _delete_find(self, key):
        return self._del_find(key, self.root)
    
    def _del_find(self, key, node):
        if node is None:
            return None
        elif node.key == key:
            return node
        elif key < node.key:
            return self._del_find(key, node.left)
        else:
            return self._del_find(key, node.right)

    def _transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        while node.left != self.null_node:
            node = node.left
        return node

    def _fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 1:
                    # case 1: x's sibling w is red
                    w.color = 0
                    x.parent.color = 1
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 0 and w.right.color == 0:
                    # case 2: x's sibling w is black, and both of w's children are black
                    w.color = 1
                    x = x.parent
                else:
                    if w.right.color == 0:
                        # case 3: x's sibling w is black, w's left child is red, and w's right child is black
                        w.left.color = 0
                        w.color = 1
                        self._right_rotate(w)
                        w = x.parent.right
                    # case 4: x's sibling w is black, and w's right child is red
                    w.color = x.parent.color
                    x.parent.color = 0
                    w.right.color = 0
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 1:
                    # case 5: x's sibling w is red
                    w.color = 0
                    x.parent.color = 1
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 0 and w.left.color == 0:
                    # case 6: x's sibling w is black, and both of w's children are black
                    w.color = 1
                    x = x.parent
                else:
                    if w.left.color == 0:
                        # case 7: x's sibling w is black, w's right child is red, and w's left child is black
                        w.right.color = 0
                        w.color = 1
                        self._left_rotate(w)
                        w = x.parent.left
                    # case 8: x's sibling w is black, and w's left child is red
                    w.color = x.parent.color
                    x.parent.color = 0
                    w.left.color = 0
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 0
        

# list_a = ['osseter', 'beleaguer', 'frounceless', 'caririan', 'nondeluding', 'jambarts', 'teledus', 'zein', 'protonematoid', 'circumstantiation', 'peribolos', 'misdiagrammed', 'unmetaphysically', 'incalculableness', 'discurre', 'catmalison', 'pyopneumoperitonitis', 'harmalin', 'constrainable', 'philanthropian']
# list_b = ["raza","hashim","fatima","tariq","hammad","nadeem","tahir"]


# fourway = RedBlackTree()
# for l in list_a:
#     fourway.insert(l)
# for n in list_b:
#     fourway.insert(n)

# # fourway.search("raza")

# # print("4way tree:")
# # # print(fourway.print_tree(fourway.root))
# # print("\n")

# # # fourway.delete(fourway.root,"raza")

# for n in list_a:
#     fourway.delete(n)
# print("Post deletion:")
# # print(fourway.print_tree(fourway.root))
# fourway.inorder()
# print("\n")