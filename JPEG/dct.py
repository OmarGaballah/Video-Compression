import numpy as np 

class DCT: 
    def __init__(self,n= 8 ) -> None:
        self.l = n
        self.weights = self.caclulate_dct_blocks()

    def caclulate_dct_blocks(self):
        dct_blocks = [] 
        for u in range(self.l): 
            for v in range(self.l): 
                block = np.zeros((self.l,self.l))
                for x in range(self.l): 
                    for y in range(self.l): 
                        block[x,y]+= np.cos((2*x+1)*u*np.pi/16)*np.cos((2*y+1)*v*np.pi/16)  
                dct_blocks.append(block)
        return dct_blocks

    def encode(self, image_slice): 
        assert np.size(image_slice) == self.l**2 , "Image size is bigger than the specidfied n for the dct block"
        
        image_slice= np.array(image_slice)
        transformed_img= np.zeros((self.l,self.l))
        # now I want to loop on (0->n-1,0->n-1)
        for u in range(self.l):
            for v in range(self.l): 
                transformed_img[u,v]= np.sum(image_slice*self.weights[u*self.l+v])
        
        # now after doing transformation we need to normalize
        transformed_img = self.normalizer(transformed_img)
        return transformed_img

    def decode(self,image_slice):
        # first of all we want to denormalize first

        image_slice= np.array(image_slice)
        org_img= np.zeros((self.l,self.l))
        # now I want to loop on (0->n-1,0->n-1)
        for u in range(self.l):
            for v in range(self.l): 
                org_img+= image_slice[u,v]*self.weights[u*self.l+v]
        
        return org_img

    def normalizer(self,img_sample): 
        img_sample[0,:]= img_sample[0,:]/2
        img_sample[:,0]= img_sample[:,0]/2   
        return img_sample/16
