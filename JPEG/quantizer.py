import numpy as np  

def read_compressor(file_loc = "low_compression.txt"):
    with open(file_loc, "r") as f: 
        data= f.read()
        data = data.replace("\n",' ')
        data= data.strip()
        data = data.split(" ")
        y= list(map(int, data)) # converting it from list of str to int
        return y 
        
class Quantizer : 
    def __init__(self,compression_Type=0) -> None:
        self.quantum = self.read_quantizer(compression_Type)

    def read_quantizer(self,compression_Type,read_func=read_compressor):
        '''
        check size and read either high or low quantizer 
        and then reshape it to the suitable size
        ''' 
        if compression_Type: # one for high compression 
            compressor =read_func("high_compression.txt")
        else :
            compressor =read_func("low_compression.txt")

        n =  int(np.sqrt(len(compressor)))
        assert n**2 == len(compressor) , " The length of the compressor is not square"
        return np.reshape(compressor,(n,n))

    def encode(self, image):
        assert np.size(image) ==  np.size(self.quantum), "Shape of the image does not match\
                                                          with the quantizer"
        return list(np.round(np.array(image)/self.quantum))

    def decoded(self,image): 
        assert np.size(image) ==  np.size(self.quantum), "Shape of the image does not match\
                                                          with the quantizer"
        return list(np.array(image)/self.quantum)                                                        





        