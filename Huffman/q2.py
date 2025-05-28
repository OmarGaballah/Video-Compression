from huffman_node import * 
from min_heap import * 


if __name__ == "__main__":

    heap_= minHeap()

    with open("Test1.txt",'r') as f: 
        for c in f.read():
            heap_.push_(Huff_node(c,1))

    head = tree_builder(heap_) # build huffman's tree
    head.inorder_traversal()   # print(symbol,freq,encoding)