import random
with open('words_alpha.txt', 'r') as file:
    
    # Read the contents of the file and split the lines into a list of words
    words_list = file.read().splitlines()
    
# Print the list of words
# print(words_list)
# print(len(words_list))

already_present = []
n = 50000
inserted = []

for i in range(n):
    repeat = False
    if repeat == False:
        x = random.randint(0,(len(words_list)-1))
        if x in already_present:
            repeat = True
        else:
            already_present.append(x)
            inserted.append(words_list[x])

# print(inserted)
# print(len(inserted),"\n")
