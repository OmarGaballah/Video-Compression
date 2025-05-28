import numpy as np
import copy
import math 

class Divide():
    def __init__(self,n= 8 ) -> None:
        self.width = n    

    def encoder(self,image):

        
        h, w = image.shape
        
        p_h = -h % self.width 
        p_w = -w % self.width 
        
        h_pad = np.floor((p_h)).astype(np.uint16)
        w_pad = np.ceil(p_w).astype(np.uint16)
        
        image_p= np.zeros((h+h_pad,w+w_pad))
        image_p[0:h,0:w]=copy.deepcopy(image)
        
        h_new, w_new = image_p.shape
        
        blocks = {}
        
        u = 0
        
        for i in range (0,h_new,self.width): 
            v = 0
            for j in range(0,w_new,self.width):
                blocks[(u,v)] = image_p[i:i+self.width,j:j+self.width]
                v +=1
            u+=1                
        return blocks

    def decoder(self,blocks,rows,cols): 
        decode_h = rows * self.width 
        decode_w = cols * self.width 
        image_after = np.zeros((decode_h,decode_w))
        u = 0
       
        for i in range (0,decode_h,self.width): 
            v = 0
            for j in range(0,decode_w,self.width):
                image_after[i:i+self.width,j:j+self.width] = blocks[(u,v)]
                v+= 1
            u+=1        
        return image_after