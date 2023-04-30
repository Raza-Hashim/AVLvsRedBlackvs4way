from AVLTree import AVLTree
from RedBlackTree import RedBlackTree
from btree import BTree
from wordreading import words_list
import random
import time
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4



list_1000 = []
list_5000 = []
list_10000 = []
list_20000 = []
list_30000 = []
list_40000 = []
list_50000 = []

del_list_1000 = []
del_list_5000 = []
del_list_10000 = []
del_list_20000 = []
del_list_30000 = []
del_list_40000 = []
del_list_50000 = []

sorted_list_1000 = []
sorted_list_5000 = []
sorted_list_10000 = []
sorted_list_20000 = []
sorted_list_30000 = []
sorted_list_40000 = []
sorted_list_50000 = []

for i in range(1000):
    sorted_list_1000.append(words_list[i])
for i in range(5000):
    sorted_list_1000.append(words_list[i])
for i in range(10000):
    sorted_list_1000.append(words_list[i])
for i in range(20000):
    sorted_list_1000.append(words_list[i])
for i in range(30000):
    sorted_list_1000.append(words_list[i])
for i in range(40000):
    sorted_list_1000.append(words_list[i])
for i in range(50000):
    sorted_list_1000.append(words_list[i])

def add_to_list(insertion_list,del_list,words_list,n):
    already_present = []
    m = int(n*0.25)
    n = int(n*0.25)
    for x in range(n):
        repeat = False
        if repeat == False:
            x = random.randint(0,(len(words_list)-1))
            if x in already_present:
                repeat = True
            else:
                already_present.append(x)
                insertion_list.append(words_list[x])

    for x in range(n):
        repeat = False
        if repeat == False:
            x = random.randint(0,(len(words_list)-1))
            if x in already_present:
                repeat = True
            else:
                already_present.append(x)
                insertion_list.append(words_list[x]) 
                del_list.append(words_list[x])            
    return

add_to_list(list_1000,del_list_1000,words_list,1000)
add_to_list(list_5000,del_list_5000,words_list,5000)
add_to_list(list_10000,del_list_10000,words_list,10000)
add_to_list(list_20000,del_list_20000,words_list,20000)
add_to_list(list_30000,del_list_30000,words_list,30000)
add_to_list(list_40000,del_list_40000,words_list,40000)
add_to_list(list_50000,del_list_50000,words_list,50000)


avl_1000 = AVLTree() 
avl_5000 = AVLTree() 
avl_10000 = AVLTree() 
avl_20000 = AVLTree() 
avl_30000 = AVLTree() 
avl_40000 = AVLTree() 
avl_50000 = AVLTree() 
redblack_1000 = RedBlackTree()
redblack_5000 = RedBlackTree()
redblack_10000 = RedBlackTree()
redblack_20000 = RedBlackTree()
redblack_30000 = RedBlackTree()
redblack_40000 = RedBlackTree()
redblack_50000 = RedBlackTree()
fourway_1000  = BTree(2)
fourway_5000  = BTree(2)
fourway_10000  = BTree(2)
fourway_20000  = BTree(2)
fourway_30000  = BTree(2)
fourway_40000  = BTree(2)
fourway_50000  = BTree(2)


# avl_insertion

avl_1000_insert_start = time.time()
for i in list_1000:
    avl_1000.insert_node(avl_1000.root,i)
avl_1000_insert_end = time.time()
avl_1000_insert = avl_1000_insert_end-avl_1000_insert_start

avl_5000_insert_start = time.time()
for i in list_5000:
    avl_5000.insert_node(avl_5000.root,i)
avl_5000_insert_end = time.time()
avl_5000_insert = avl_5000_insert_end-avl_5000_insert_start

avl_10000_insert_start = time.time()
for i in list_10000:
    avl_10000.insert_node(avl_10000.root,i)
avl_10000_insert_end = time.time()
avl_10000_insert = avl_10000_insert_end-avl_10000_insert_start

avl_20000_insert_start = time.time()
for i in list_20000:
    avl_20000.insert_node(avl_20000.root,i)
avl_20000_insert_end = time.time()
avl_20000_insert = avl_20000_insert_end-avl_20000_insert_start

avl_30000_insert_start = time.time()
for i in list_30000:
    avl_30000.insert_node(avl_30000.root,i)
avl_30000_insert_end = time.time()
avl_30000_insert = avl_30000_insert_end-avl_30000_insert_start

avl_40000_insert_start = time.time()
for i in list_40000:
    avl_40000.insert_node(avl_40000.root,i)
avl_40000_insert_end = time.time()
avl_40000_insert = avl_40000_insert_end-avl_40000_insert_start

avl_50000_insert_start = time.time()
for i in list_50000:
    avl_50000.insert_node(avl_50000.root,i)
avl_50000_insert_end = time.time()
avl_50000_insert = avl_50000_insert_end-avl_50000_insert_start


#avl traversal

# avl_1000_traversal_start = time.time()
# avl_1000.in_order_traversal(avl_1000.root)
# avl_1000_traversal_end = time.time()
# avl_1000_traversal = avl_1000_traversal_end-avl_1000_traversal_start

# avl_5000_traversal_start = time.time()
# avl_5000.in_order_traversal(avl_5000.root)
# avl_5000_traversal_end = time.time()
# avl_5000_traversal = avl_5000_traversal_end-avl_5000_traversal_start

# avl_10000_traversal_start = time.time()
# avl_10000.in_order_traversal(avl_10000.root)
# avl_10000_traversal_end = time.time()
# avl_10000_traversal = avl_10000_traversal_end-avl_10000_traversal_start

# avl_20000_traversal_start = time.time()
# avl_20000.in_order_traversal(avl_20000.root)
# avl_20000_traversal_end = time.time()
# avl_20000_traversal = avl_20000_traversal_end-avl_20000_traversal_start

# avl_30000_traversal_start = time.time()
# avl_30000.in_order_traversal(avl_30000.root)
# avl_30000_traversal_end = time.time()
# avl_30000_traversal = avl_30000_traversal_end-avl_30000_traversal_start

# avl_40000_traversal_start = time.time()
# avl_40000.in_order_traversal(avl_40000.root)
# avl_40000_traversal_end = time.time()
# avl_40000_traversal = avl_40000_traversal_end-avl_40000_traversal_start

# avl_50000_traversal_start = time.time()
# avl_50000.in_order_traversal(avl_50000.root)
# avl_50000_traversal_end = time.time()
# avl_50000_traversal = avl_50000_traversal_end-avl_50000_traversal_start


# # avl find
# root = None
# avl_1000_find_start = time.time()
# for i in del_list_1000:
#     avl_1000.search(i)
# avl_1000_find_end = time.time()
# avl_1000_find = avl_1000_find_end - avl_1000_find_start

# avl_5000_find_start = time.time()
# for i in del_list_5000:
#     avl_5000.search(i)
# avl_5000_find_end = time.time()
# avl_5000_find = avl_5000_find_end - avl_5000_find_start

# avl_10000_find_start = time.time()
# for i in del_list_10000:
#     avl_10000.search(i)
# avl_10000_find_end = time.time()
# avl_10000_find = avl_10000_find_end - avl_10000_find_start

# avl_20000_find_start = time.time()
# for i in del_list_20000:
#     avl_20000.search(i)
# avl_20000_find_end = time.time()
# avl_20000_find = avl_20000_find_end - avl_20000_find_start

# avl_30000_find_start = time.time()
# for i in del_list_30000:
#     avl_30000.search(i)
# avl_30000_find_end = time.time()
# avl_30000_find = avl_30000_find_end - avl_30000_find_start

# avl_40000_find_start = time.time()
# for i in del_list_40000:
#     avl_40000.search(i)
# avl_40000_find_end = time.time()
# avl_40000_find = avl_40000_find_end - avl_40000_find_start

# avl_50000_find_start = time.time()
# for i in del_list_50000:
#     avl_50000.search(i)
# avl_50000_find_end = time.time()
# avl_50000_find = avl_50000_find_end - avl_50000_find_start


# avl deletion
root = None
avl_1000_del_start = time.time_ns()
for i in del_list_1000:
    avl_1000.delete_node(root,i)
avl_1000_del_end = time.time_ns()
avl_1000_del = avl_1000_del_end - avl_1000_del_start

avl_5000_del_start = time.time_ns()
for i in del_list_5000:
    avl_5000.delete_node(root,i)
avl_5000_del_end = time.time_ns()
avl_5000_del = avl_5000_del_end - avl_5000_del_start

avl_10000_del_start = time.time_ns()
for i in del_list_10000:
    avl_10000.delete_node(root,i)
avl_10000_del_end = time.time_ns()
avl_10000_del = avl_10000_del_end - avl_10000_del_start

avl_20000_del_start = time.time_ns()
for i in del_list_20000:
    avl_20000.delete_node(root,i)
avl_20000_del_end = time.time_ns()
avl_20000_del = avl_20000_del_end - avl_20000_del_start

avl_30000_del_start = time.time_ns()
for i in del_list_30000:
    avl_30000.delete_node(root,i)
avl_30000_del_end = time.time_ns()
avl_30000_del = avl_30000_del_end - avl_30000_del_start

avl_40000_del_start = time.time_ns()
for i in del_list_40000:
    avl_40000.delete_node(root,i)
avl_40000_del_end = time.time_ns()
avl_40000_del = avl_40000_del_end - avl_40000_del_start

avl_50000_del_start = time.time_ns()
for i in del_list_50000:
    avl_50000.delete_node(root,i)
avl_50000_del_end = time.time_ns()
avl_50000_del = avl_50000_del_end - avl_50000_del_start


#redblack_insertion

redblack_1000_insert_start = time.time()
for i in list_1000:
    redblack_1000.insert(i)
redblack_1000_insert_end = time.time()
redblack_1000_insert = redblack_1000_insert_end-redblack_1000_insert_start

redblack_5000_insert_start = time.time()
for i in list_5000:
    redblack_5000.insert(i)
redblack_5000_insert_end = time.time()
redblack_5000_insert = redblack_5000_insert_end-redblack_5000_insert_start

redblack_10000_insert_start = time.time()
for i in list_10000:
    redblack_10000.insert(i)
redblack_10000_insert_end = time.time()
redblack_10000_insert = redblack_10000_insert_end-redblack_10000_insert_start

redblack_20000_insert_start = time.time()
for i in list_20000:
    redblack_20000.insert(i)
redblack_20000_insert_end = time.time()
redblack_20000_insert = redblack_20000_insert_end-redblack_20000_insert_start

redblack_30000_insert_start = time.time()
for i in list_30000:
    redblack_30000.insert(i)
redblack_30000_insert_end = time.time()
redblack_30000_insert = redblack_30000_insert_end-redblack_30000_insert_start

redblack_40000_insert_start = time.time()
for i in list_40000:
    redblack_40000.insert(i)
redblack_40000_insert_end = time.time()
redblack_40000_insert = redblack_40000_insert_end-redblack_40000_insert_start

redblack_50000_insert_start = time.time()
for i in list_50000:
    redblack_50000.insert(i)
redblack_50000_insert_end = time.time()
redblack_50000_insert = redblack_50000_insert_end-redblack_50000_insert_start


#redblack traversal

# redblack_1000_traversal_start = time.time()
# redblack_1000.inorder()
# redblack_1000_traversal_end = time.time()
# redblack_1000_traversal = redblack_1000_traversal_end-redblack_1000_traversal_start

# redblack_5000_traversal_start = time.time()
# redblack_5000.inorder()
# redblack_5000_traversal_end = time.time()
# redblack_5000_traversal = redblack_5000_traversal_end-redblack_5000_traversal_start

# redblack_10000_traversal_start = time.time()
# redblack_10000.inorder()
# redblack_10000_traversal_end = time.time()
# redblack_10000_traversal = redblack_10000_traversal_end-redblack_10000_traversal_start

# redblack_20000_traversal_start = time.time()
# redblack_20000.inorder()
# redblack_20000_traversal_end = time.time()
# redblack_20000_traversal = redblack_20000_traversal_end-redblack_20000_traversal_start

# redblack_30000_traversal_start = time.time()
# redblack_30000.inorder()
# redblack_30000_traversal_end = time.time()
# redblack_30000_traversal = redblack_30000_traversal_end-redblack_30000_traversal_start

# redblack_40000_traversal_start = time.time()
# redblack_40000.inorder()
# redblack_40000_traversal_end = time.time()
# redblack_40000_traversal = redblack_40000_traversal_end-redblack_40000_traversal_start

# redblack_50000_traversal_start = time.time()
# redblack_50000.inorder()
# redblack_50000_traversal_end = time.time()
# redblack_50000_traversal = redblack_50000_traversal_end-redblack_50000_traversal_start


# # redblack search
# root = None
# redblack_1000_find_start = time.time()
# for i in del_list_1000:
#     redblack_1000.find(i)
# redblack_1000_find_end = time.time()
# redblack_1000_find = redblack_1000_find_end - redblack_1000_find_start

# redblack_5000_find_start = time.time()
# for i in del_list_5000:
#     redblack_5000.find(i)
# redblack_5000_find_end = time.time()
# redblack_5000_find = redblack_5000_find_end - redblack_5000_find_start

# redblack_10000_find_start = time.time()
# for i in del_list_10000:
#     redblack_10000.find(i)
# redblack_10000_find_end = time.time()
# redblack_10000_find = redblack_10000_find_end - redblack_10000_find_start

# redblack_20000_find_start = time.time()
# for i in del_list_20000:
#     redblack_20000.find(i)
# redblack_20000_find_end = time.time()
# redblack_20000_find = redblack_20000_find_end - redblack_20000_find_start

# redblack_30000_find_start = time.time()
# for i in del_list_30000:
#     redblack_30000.find(i)
# redblack_30000_find_end = time.time()
# redblack_30000_find = redblack_30000_find_end - redblack_30000_find_start

# redblack_40000_find_start = time.time()
# for i in del_list_40000:
#     redblack_40000.find(i)
# redblack_40000_find_end = time.time()
# redblack_40000_find = redblack_40000_find_end - redblack_40000_find_start

# redblack_50000_find_start = time.time()
# for i in del_list_50000:
#     redblack_50000.find(i)
# redblack_50000_find_end = time.time()
# redblack_50000_find = redblack_50000_find_end - redblack_50000_find_start


###redblack deletion
root = None
redblack_1000_del_start = time.time_ns()
for i in del_list_1000:
    redblack_1000.delete(i)
redblack_1000_del_end = time.time_ns()
redblack_1000_del = redblack_1000_del_end - redblack_1000_del_start

redblack_5000_del_start = time.time_ns()
for i in del_list_5000:
    redblack_5000.delete(i)
redblack_5000_del_end = time.time_ns()
redblack_5000_del = redblack_5000_del_end - redblack_5000_del_start

redblack_10000_del_start = time.time_ns()
for i in del_list_10000:
    redblack_10000.delete(i)
redblack_10000_del_end = time.time_ns()
redblack_10000_del = redblack_10000_del_end - redblack_10000_del_start

redblack_20000_del_start = time.time_ns()
for i in del_list_20000:
    redblack_20000.delete(i)
redblack_20000_del_end = time.time_ns()
redblack_20000_del = redblack_20000_del_end - redblack_20000_del_start

redblack_30000_del_start = time.time_ns()
for i in del_list_30000:
    redblack_30000.delete(i)
redblack_30000_del_end = time.time_ns()
redblack_30000_del = redblack_30000_del_end - redblack_30000_del_start

redblack_40000_del_start = time.time_ns()
for i in del_list_40000:
    redblack_40000.delete(i)
redblack_40000_del_end = time.time_ns()
redblack_40000_del = redblack_40000_del_end - redblack_40000_del_start

redblack_50000_del_start = time.time_ns()
for i in del_list_50000:
    redblack_50000.delete(i)
redblack_50000_del_end = time.time_ns()
redblack_50000_del = redblack_50000_del_end - redblack_50000_del_start

# fourway_insertion

fourway_1000_insert_start = time.time()
for i in list_1000:
    fourway_1000.insert(i)
fourway_1000_insert_end = time.time()
fourway_1000_insert = fourway_1000_insert_end-fourway_1000_insert_start

fourway_5000_insert_start = time.time()
for i in list_5000:
    fourway_5000.insert(i)
fourway_5000_insert_end = time.time()
fourway_5000_insert = fourway_5000_insert_end-fourway_5000_insert_start

fourway_10000_insert_start = time.time()
for i in list_10000:
    fourway_10000.insert(i)
fourway_10000_insert_end = time.time()
fourway_10000_insert = fourway_10000_insert_end-fourway_10000_insert_start

fourway_20000_insert_start = time.time()
for i in list_20000:
    fourway_20000.insert(i)
fourway_20000_insert_end = time.time()
fourway_20000_insert = fourway_20000_insert_end-fourway_20000_insert_start

fourway_30000_insert_start = time.time()
for i in list_30000:
    fourway_30000.insert(i)
fourway_30000_insert_end = time.time()
fourway_30000_insert = fourway_30000_insert_end-fourway_30000_insert_start

fourway_40000_insert_start = time.time()
for i in list_40000:
    fourway_40000.insert(i)
fourway_40000_insert_end = time.time()
fourway_40000_insert = fourway_40000_insert_end-fourway_40000_insert_start

fourway_50000_insert_start = time.time()
for i in list_50000:
    fourway_50000.insert(i)
fourway_50000_insert_end = time.time()
fourway_50000_insert = fourway_50000_insert_end-fourway_50000_insert_start


# ## fourway traversal

# fourway_1000_traversal_start = time.time()
# print(fourway_1000.inorder_traversal())
# fourway_1000_traversal_end = time.time()
# fourway_1000_traversal = fourway_1000_traversal_end-fourway_1000_traversal_start

# fourway_5000_traversal_start = time.time()
# print(fourway_5000.inorder_traversal())
# fourway_5000_traversal_end = time.time()
# fourway_5000_traversal = fourway_5000_traversal_end-fourway_5000_traversal_start

# fourway_10000_traversal_start = time.time()
# print(fourway_10000.inorder_traversal())
# fourway_10000_traversal_end = time.time()
# fourway_10000_traversal = fourway_10000_traversal_end-fourway_10000_traversal_start

# fourway_20000_traversal_start = time.time()
# print(fourway_20000.inorder_traversal())
# fourway_20000_traversal_end = time.time()
# fourway_20000_traversal = fourway_20000_traversal_end-fourway_20000_traversal_start

# fourway_30000_traversal_start = time.time()
# print(fourway_30000.inorder_traversal())
# fourway_30000_traversal_end = time.time()
# fourway_30000_traversal = fourway_30000_traversal_end-fourway_30000_traversal_start

# fourway_40000_traversal_start = time.time()
# print(fourway_40000.inorder_traversal())
# fourway_40000_traversal_end = time.time()
# fourway_40000_traversal = fourway_40000_traversal_end-fourway_40000_traversal_start

# fourway_50000_traversal_start = time.time()
# print(fourway_50000.inorder_traversal())
# fourway_50000_traversal_end = time.time()
# fourway_50000_traversal = fourway_50000_traversal_end-fourway_50000_traversal_start


# ## Fourway search


# root = None
# fourway_1000_find_start = time.time()
# for i in del_list_1000:
#     fourway_1000.search(i)
# fourway_1000_find_end = time.time()
# fourway_1000_find = fourway_1000_find_end - fourway_1000_find_start

# fourway_5000_find_start = time.time()
# for i in del_list_5000:
#     fourway_5000.search(i)
# fourway_5000_find_end = time.time()
# fourway_5000_find = fourway_5000_find_end - fourway_5000_find_start

# fourway_10000_find_start = time.time()
# for i in del_list_10000:
#     fourway_10000.search(i)
# fourway_10000_find_end = time.time()
# fourway_10000_find = fourway_10000_find_end - fourway_10000_find_start

# fourway_20000_find_start = time.time()
# for i in del_list_20000:
#     fourway_20000.search(i)
# fourway_20000_find_end = time.time()
# fourway_20000_find = fourway_20000_find_end - fourway_20000_find_start

# fourway_30000_find_start = time.time()
# for i in del_list_30000:
#     fourway_30000.search(i)
# fourway_30000_find_end = time.time()
# fourway_30000_find = fourway_30000_find_end - fourway_30000_find_start

# fourway_40000_find_start = time.time()
# for i in del_list_40000:
#     fourway_40000.search(i)
# fourway_40000_find_end = time.time()
# fourway_40000_find = fourway_40000_find_end - fourway_40000_find_start

# fourway_50000_find_start = time.time()
# for i in del_list_50000:
#     fourway_50000.search(i)
# fourway_50000_find_end = time.time()
# fourway_50000_find = fourway_50000_find_end - fourway_50000_find_start

#fourway deletion
# root = None
# fourway_1000_del_start = time.time_ns()
# for i in del_list_1000:
#     fourway_1000.delete(i)
# fourway_1000_del_end = time.time_ns()
# fourway_1000_del = fourway_1000_del_end - fourway_1000_del_start

# fourway_5000_del_start = time.time_ns()
# for i in del_list_5000:
#     fourway_5000.delete(i)
# fourway_5000_del_end = time.time_ns()
# fourway_5000_del = fourway_5000_del_end - fourway_5000_del_start

# fourway_10000_del_start = time.time_ns()
# for i in del_list_10000:
#     fourway_10000.delete(i)
# fourway_10000_del_end = time.time_ns()
# fourway_10000_del = fourway_10000_del_end - fourway_10000_del_start

# fourway_20000_del_start = time.time_ns()
# for i in del_list_20000:
#     fourway_20000.delete(i)
# fourway_20000_del_end = time.time_ns()
# fourway_20000_del = fourway_20000_del_end - fourway_20000_del_start

# fourway_30000_del_start = time.time_ns()
# for i in del_list_30000:
#     fourway_30000.delete(i)
# fourway_30000_del_end = time.time_ns()
# fourway_30000_del = fourway_30000_del_end - fourway_30000_del_start

# fourway_40000_del_start = time.time_ns()
# for i in del_list_40000:
#     fourway_40000.delete(i)
# fourway_40000_del_end = time.time_ns()
# fourway_40000_del = fourway_40000_del_end - fourway_40000_del_start

# fourway_50000_del_start = time.time_ns()
# for i in del_list_50000:
#     fourway_50000.delete(i)
# fourway_50000_del_end = time.time_ns()
# fourway_50000_del = fourway_50000_del_end - fourway_50000_del_start









# graphing

sizes = [1000,5000,10000,20000,30000,40000,50000]

avl_insertion_times = [avl_1000_insert,avl_5000_insert,avl_10000_insert,avl_20000_insert,avl_30000_insert,avl_40000_insert,avl_50000_insert]
# avl_traversal_times = [avl_1000_traversal,avl_5000_traversal,avl_10000_traversal,avl_20000_traversal,avl_30000_traversal,avl_40000_traversal,avl_50000_traversal]
# avl_search_times = [avl_1000_find,avl_5000_find,avl_10000_find,avl_20000_find,avl_30000_find,avl_40000_find,avl_50000_find]
avl_del_times = [avl_1000_del,avl_5000_del,avl_10000_del,avl_20000_del,avl_30000_del,avl_40000_del,avl_50000_del]


redblack_insertion_times = [redblack_1000_insert,redblack_5000_insert,redblack_10000_insert,redblack_20000_insert,redblack_30000_insert,redblack_40000_insert,redblack_50000_insert]
# redblack_traversal_times = [redblack_1000_traversal,redblack_5000_traversal,redblack_10000_traversal,redblack_20000_traversal,redblack_30000_traversal,redblack_40000_traversal,redblack_50000_traversal]
# redblack_search_times = [redblack_1000_find,redblack_5000_find,redblack_10000_find,redblack_20000_find,redblack_30000_find,redblack_40000_find,redblack_50000_find]
redblack_del_times = [redblack_1000_del,redblack_5000_del,redblack_10000_del,redblack_20000_del,redblack_30000_del,redblack_40000_del,redblack_50000_del]


fourway_insertion_times = [fourway_1000_insert,fourway_5000_insert,fourway_10000_insert,fourway_20000_insert,fourway_30000_insert,fourway_40000_insert,fourway_50000_insert]
# fourway_traversal_times = [fourway_1000_traversal,fourway_5000_traversal,fourway_10000_traversal,fourway_20000_traversal,fourway_30000_traversal,fourway_40000_traversal,fourway_50000_traversal]
# fourway_search_times = [fourway_1000_find,fourway_5000_find,fourway_10000_find,fourway_20000_find,fourway_30000_find,fourway_40000_find,fourway_50000_find]
# fourway_del_times = [fourway_1000_del,fourway_5000_del,fourway_10000_del,fourway_20000_del,fourway_30000_del,fourway_40000_del,fourway_50000_del]




# plt.plot(sizes,avl_insertion_times,label="AVL Insertion")
# plt.plot(sizes,redblack_insertion_times,label="RedBlack Insertion")
# plt.plot(sizes,fourway_insertion_times,label="FourWay Insertion")

# print("\n", avl_insertion_times)
# print(redblack_insertion_times)
# print(fourway_insertion_times)


# plt2.plot(sizes,avl_traversal_times,label="AVL Traversal")
# plt2.plot(sizes,redblack_traversal_times,label="RedBlack Traversal")
# plt2.plot(sizes,fourway_traversal_times,label="FourWay Traversal")

# print("\n", avl_traversal_times)
# print(redblack_traversal_times)
# print(fourway_traversal_times)


# plt3.plot(sizes,avl_search_times,label="AVL search")
# plt3.plot(sizes,redblack_search_times,label="RedBlack search")
# plt3.plot(sizes,fourway_search_times,label="FourWay search")

# print("\n", avl_search_times)
# print(redblack_search_times)
# print(fourway_search_times)

plt4.plot(sizes,avl_del_times,label="AVL delete")
plt4.plot(sizes,redblack_del_times,label="RedBlack delete")
# plt4.plot(sizes,fourway_del_times,label="FourWay delete")

print("\n", avl_del_times)
print(redblack_del_times)
#print(fourway_del_times)

plt4.legend()
plt4.show()

# plt2.legend()
# plt2.show()

# plt3.legend()
# plt3.show()



