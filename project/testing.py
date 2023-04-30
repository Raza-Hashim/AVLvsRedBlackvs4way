# from wordreading import inserted
# from AVLTree import AVLTree
# from RedBlackTree import RedBlackTree
# from btree import BTree

# list_a = []
# list_b = ["raza","hashim","fatima","tariq","hammad","nadeem","tahir","ghazi"]
# for i in range(len(inserted)-1):
#     # list_a.append((inserted[i],inserted[i]))
#     list_a.append(inserted[i])

# # fourway = BTree(2)
# # # for l in list_a:
# # #     fourway.insert(l)
# # for n in list_b:
# #     fourway.insert(n)

# # print("4way tree:")
# # fourway.print_order()
# # # print(fourway.inorder_traversal())
# # print("\n")

# # for n in list_b:
# #     fourway.delete(n)
# # print("Post deletion:")
# # fourway.print_order()
# # # print(fourway.inorder_traversal())
# # print("\n")

# # redblack = RedBlackTree()
# # for k in list_a:
# #     redblack.insert(k)
# # for n in list_b:
# #     redblack.insert(n)

# # print("Redblack:")
# # redblack.inorder()
# # print("\n")
# # for m in list_b:
# #     redblack.delete(m)
# # print("post deletion")
# # redblack.inorder()


# root = None
# avl = AVLTree()
# for j in list_a:
#     root = avl.insert_node(root,j)
# for h in list_b:
#     root = avl.insert_node(root,h)
# print("AVL: \n")
# avl.in_order_traversal(root)
# print("\n")
# print(avl.root.key)
# print(avl.search("raza"))
# print("\n")
# for h in list_b:
#     root = avl.delete_node(root,h)
# print("post deletion \n")
# avl.in_order_traversal(root)
# print("\n")   
# # print(avl.root.key)
# # print(avl.search("raza"))


# # redblack.insert("raza")
# # print("Redblack:")
# # redblack.inorder()
# # print("\n")

# # print(redblack.find("raza"))

# # fourway.insert("eza")
# # print(fourway.inorder_traversal())
# # print(fourway.search("eza"))