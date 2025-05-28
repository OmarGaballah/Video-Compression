import numpy as np 

class Zigzager():
    def __init__(self,n= 8 ) -> None:
        self.width = n
        self.indices = self._init()
    
    def _init(self):
        idx_newOrder= { _:[] for _ in range(2*self.width -1)}
        for i in range(self.width): 
            for j in range(self.width): 
                sum = i+j 
                if (sum %2 == 1): 
                    idx_newOrder[i+j].append(i*self.width+j)
                else : 
                    idx_newOrder[i+j].insert(0,i*self.width+j)
            
        
        # now we have the indices oredred in a zigzag value and we 
        # want to set them in one list 
        solution = [] 
        for i in range(2*self.width-1): 
            solution.extend(idx_newOrder[i])
        return solution



    def encoder(self,image)-> list:
        # let's rehsape the image to be 1D array
        # and then we will use the self.indices to
        # reorder the image in a zigzag way
        
        assert np.size(image) == self.width**2 , f"The image size does not match {self.width**2}"        
        
        image= np.reshape(image,(-1,)) 
        newimage= np.zeros(image.shape)
        for i,v in enumerate(image): 
            newimage[i] = image[self.indices[i]]
        return list(newimage)

    def decoder(self,serial_img): 
        assert np.size(serial_img) == self.width**2 , f"The image len does not match {self.width**2}"

        org_img = np.zeros(self.width**2)
        for i,v in enumerate(serial_img): 
            org_img[self.indices[i]] = v
        
        org_img = np.reshape(org_img,(self.width,self.width))
        return list(org_img)
    