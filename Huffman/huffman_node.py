
'''
- sort array of symbols
- Make leaf nodde from the lowest  2 symbols 
- 
'''

from typing import List
import math


class Huff_node: 
    def __init__(self,symbol,freq,left=None,right=None) -> None:
        self.symbol = symbol
        self.freq = freq if not left or not right else left.freq+right.freq 
        
        self.left= left
        self.right= right

    def __eq__(self, other_node: object) -> bool:
        return self.symbol == other_node.symbol  
    def __gt__(self,other) -> bool:
        return self.freq > other.freq
    def __ge__(self,other) -> bool:
        return self.freq >= other.freq
    def __add__(self, other) -> int:
         return self.freq + other.freq 
       
    def inorder_traversal(self):
        if self.left: 
            self.left.inorder_traversal_helper('1')
        if self.right: 
            self.right.inorder_traversal_helper('0')

    def inorder_traversal_helper(self,encoding):
        self.encoding = encoding
        if self.left: 
            self.left.inorder_traversal_helper(self.encoding + '1')  
        if self.right:
            self.right.inorder_traversal_helper(self.encoding + '0') 
        if not (self.left and self.right): 
            print(f"symbol: {self.symbol} , freq: {self.freq} , encoding:{self.encoding}")

class Encoder: 
    def __init__(self) -> None:
        self.encoder_list= []
        self.frequency_list = {}
        self.isfitted= False
    def encode(self,head:Huff_node)->List:
        self.encoder_list = []
        self.frequency_list = {}
        try:
            self.inorder_traversal(head)
        
        except: 
            print("Kindly pass a hufmman node object ")
            return []
        
        self.isfitted = True
        return self.encoder_list


    def avg_code_length(self)->float:
        if self.isfitted:
            mean = 0
            for symbol,encoding in self.encoder_list: 
                mean += len(encoding) * self.frequency_list[symbol]
            return mean
        else: 
            print("You cannot calc avg code length before fitting")
            return 
    
    def entropy(self)->float:
        if self.isfitted:
            entropy_ = 0
            for symbol,encoding in self.encoder_list: 
                entropy_ -= self.frequency_list[symbol]*math.log2(self.frequency_list[symbol])
            return entropy_
        else: 
            print("You cannot entropy before fitting")
            return 


    def inorder_traversal(self,head)->None:
        if head.left: 
            self.inorder_traversal_helper(head.left,'1')
        if head.right: 
            self.inorder_traversal_helper(head.right,'0')
    
    def inorder_traversal_helper(self,node:Huff_node,encoding:str)->None:
        node.encoding = encoding
        if node.left: 
            self.inorder_traversal_helper(node.left,node.encoding + '1')  
        if node.right:
            self.inorder_traversal_helper(node.right,node.encoding + '0') 
        if not (node.left and node.right): 
            self.encoder_list.append((node.symbol,node.encoding))
            self.frequency_list[node.symbol] = node.freq
            #print(f"symbol: {node.symbol} , freq: {node.freq} , encoding:{node.encoding}")
            print("symbol: %s , freq: %0.5f, encoding: %s"%(node.symbol,node.freq,node.encoding))


if __name__=="__main__" :
    h1 = Huff_node("a",10)
    h2 = Huff_node("a",5)
    h3 = Huff_node("b",7)
    print("hereee")
    print(h3.freq)


