from huffman_node import * 
from min_heap import * 


##################################################
#           Design Standards                     #
#   1. read all the symbols and their            #
#      coresspond frequencies                    #
#   2. Initialize the min heap_                  #
#   3. Construct the encoder algorithm           #
##################################################

h1 = Huff_node("a",5)
h2 = Huff_node("b",5)
h3 = Huff_node("c",7)
h4 = Huff_node("d",1)
h5 = Huff_node("a",15)


heap_ = minHeap()

heap_.push_(h1)
heap_.push_(h2)
heap_.push_(h3)
heap_.push_(h4)
heap_.push_(h5)


cond = True
i= 0 
while cond:
    i+= 1 
    node = heap_.extract_min()
    if node:
        print(node.symbol,node.freq)
    else: 
        cond= False

heap_.push_(h1)
heap_.push_(h2)
heap_.push_(h3)
heap_.push_(h4)
heap_.push_(h5)

head = tree_builder(heap_)
head.inorder_traversal()