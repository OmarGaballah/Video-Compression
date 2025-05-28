from JPEG.dct import DCT
from JPEG.zigzag import Zigzager
from JPEG.Run_Length import RunLength
from JPEG.quantizer import Quantizer
from JPEG.Divide import Divide
import numpy as np

class JPEG: 
    def __init__(self,n=8,compression_Type=0) -> None:
        self.DCT_ = DCT(n)
        self.divide = Divide(n)
        self.quantizer = Quantizer(compression_Type=compression_Type)
        self.zigzag= Zigzager(n)
        self.runlength= RunLength()
    
    def compress(self,img):
        img = np.array(img)
        rows,cols = img.shape
        rows = int(np.ceil(rows/self.divide.width))
        cols = int(np.ceil(cols/self.divide.width))

        encodedsamples= []

        img_samples = self.divide.encoder(img)
        for i in range(rows): 
            for j in range(cols): 
                t= (i,j)
                dct_img= self.DCT_.encode(img_samples[t])
                quan_img= self.quantizer.encode(dct_img)
                img_1d= self.zigzag.encoder(quan_img)
                encodedsamples.extend(img_1d)
        
        encodedsamples= self.runlength.encoder(encodedsamples)
        return encodedsamples
    
    def decompress(self,compressed_image,rows,cols):
        imgs = {}
        img_1d = self.runlength.decoder(compressed_image)
        img_1d =np.reshape(img_1d,(rows*cols,self.divide.width**2))

        for i in range(rows): 
            for j in range(cols):
                t= (i,j)
                img_= self.zigzag.decoder(img_1d[i*cols+j,:])
                unquan_img= self.quantizer.decoded(img_)
                dct_img= self.DCT_.decode(unquan_img)
                imgs[t] = dct_img
        return self.divide.decoder(imgs,rows,cols)




        