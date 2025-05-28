from multiprocessing.pool import TERMINATE
from pickle import FALSE, TRUE
from huffman_node import *

class minHeap:
    def __init__(self) -> None:
        self.size= 0 
        self.heap = [] 
    def push_(self,node): 
        self.size+=1
        # if a certain node is already in the list then 
        # i want to remove it and add it after reorganising the 
        if node in self.heap:
            self.remove_a_duplicate(node) 
            self.size -= 1 
        if not self.heap: 
            self.heap.append(node)
            return 
        self.insert_node(node)
        return 
    
    def extract_min(self):
        if self.size == 0: return None
        
        self.size-= 1  
        return self.heap.pop(0)

    def remove_a_duplicate(self,node): 
        for i,v in enumerate(self.heap): 
            if v == node: 
                node.freq += v.freq
                self.heap.remove(v)
                return 
        return None
    def insert_node(self,node): 
        # if the list has alreaddy some elements 
        # then we want to put it before the bigger values
        for i,v in enumerate(self.heap): 
            if v > node:
                self.heap.insert(i,node)
                return
        self.heap.append(node)
        return 

    def normalize(self)->None: 
        sum = 0
        for node in self.heap:
            sum+= node.freq
        for node in self.heap: 
            node.freq /= sum
        return 


def tree_builder(heap_: minHeap): 
    counter = 0
    s_node = heap_.extract_min()
    s2_node = heap_.extract_min()

    head = Huff_node(f"N{counter}",0,s_node,s2_node) 
    heap_.push_(head)
    counter+=1
    
    while heap_.size > 1: 

        s_node = heap_.extract_min()
        s2_node = heap_.extract_min()
              

        head = Huff_node(f"N{counter}",0,s_node,s2_node)
        heap_.push_(head)
        counter+=1

    return head
        
