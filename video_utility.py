import cv2 
import numpy as np
from JPEG.Divide import Divide



def motion_estimate(current_frame,ref_frame,size= 16,searh_space=9): 
    
    divider= Divide(n= size)
    cur_frames= divider.encoder(current_frame)
    
    rows,cols = ref_frame.shape
    rows_blocks = int(np.ceil(rows/size))
    cols_blocks = int(np.ceil(cols/size))
    
    motion_vector = dict()
    for i in range(rows_blocks):
        for j in range(cols_blocks):
            cframe = cur_frames[(i,j)]
            best_match = np.inf
            
            cap_i = i*size+searh_space if i*size+searh_space+size < rows else rows-size
            cap_j = j*size+searh_space if j*size+searh_space+size < cols else cols-size

            i_list = list(range(max(i*size-searh_space,0),cap_i)) #i_start and i_end
            j_list = list(range(max(j*size-searh_space,0),cap_j)) #start_j and end_j
            for u in (i_list):
                for v in (j_list):
                    if best_match == -1: 
                        continue
                    mse = np.mean((cframe - ref_frame[u:u+size,v:v+size])**2)
                    if mse == 0: 
                        best_match = -1 
                        best= (u,v)
                    elif mse < best_match: 
                        best_match = mse
                        best = (u,v)
            motion_vector[(i,j)] = best
    return motion_vector



def compensator(motion_vector,ref_image,size,rows,cols): 
    Predication = {}
    for key in (motion_vector):
        u,v = motion_vector[key] #
        Predication[key] = ref_image[u:u+ size,v: v+size]
    return Divide(size).decoder(Predication,rows,cols)
        