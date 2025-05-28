import math

class RunLength():
    def __init__(self ) -> None:
        return None
    def encoder(self,array)-> list:
        counter = 0 
        new = []
        blocks_after = {}
    #    dict_len = int(math.sqrt(len(blocks)))
    #   decode_h = dict_len * self.width                    
        for i in range (0,len(array)):
            if array[i] == 0:
                counter += 1     
            if array[i] != 0 and counter >= 1:
                new.append(0)
                new.append(counter)
                new.append(array[i])
                counter = 0   
            elif array[i] != 0 and counter == 0:
                new.append(array[i])
            elif array[-1] == 0 and counter >= 1 and i == (len(array) - 1):
                new.append(0)
                new.append(counter)
                counter = 0  
            if array[i] == 0 and i == len(array) - 1 and array[i-1] != 0 :
                new.append(0)
                new.append(1)
        return new


    def decoder(self,new): 
        old = []
        for i in range (0,len(new)):
            if new[i] == 0:
                for _ in range (0,new[i+1]-1):
                    old.append(0)

            if new[i] ==0 or new[i-1] != 0:
                old.append(new[i])
        return old