from huffman_node import * 
from min_heap import * 

eng_char__freq= [("E", 12.02),("T",9.10),("A",8.12),("O",7.68),("I",7.31),\
    ("N",6.95),("S",6.28),("R",6.02),("H",5.92),("D",4.32),("L",3.98),\
    ("U",2.88),("C",2.71),("M",2.61),("F",2.30),("Y",2.11),("W",2.09),\
    ("G",2.03),("P",1.82),("B",1.49),("V",1.11),("K",0.69),("X",0.17),\
    ("Q",0.11),("J",0.10),("Z",0.07)]

if __name__ == "__main__":
    heap_ = minHeap()
    
    # construct the min heap to
    # arrange sybols ascending according to
    # thier freq
    for (symbol,freq) in  eng_char__freq: 
        heap_.push_(Huff_node(symbol,freq))

    head = tree_builder(heap_) # build huffman's tree
    head.inorder_traversal()   # print(symbol,freq,encoding)

