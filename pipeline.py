import cv2
import numpy as np
from video_utility import motion_estimate,compensator
from JPEG.jpeg_pipeline import JPEG
from JPEG.Divide import Divide



def get_motion_vetor(motion_list,row,col):
    motion_vec_dict =dict()
    i=0
    for u in range(row):
        for v in range(col): 
            motion_vec_dict[(u,v)] = (motion_list[i],motion_list[i+1])
            i+=2
    return motion_vec_dict



def capture_frame(video_cap,num):
    video_cap.set(cv2.CAP_PROP_POS_FRAMES,num)
    _, frame = video_cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    return frame

def video_compression(video_link,temp_size,search_space,jpeg_size=8,compression_type=0):
    print("----------------STARTED----------------")
    divider= Divide(n= temp_size)
    video_cap = cv2.VideoCapture(video_link)
    frame_count = video_cap.get(cv2.CAP_PROP_FRAME_COUNT)
    compressed = list()
    
    jpeg= JPEG(jpeg_size,compression_type)

    frame0= capture_frame(video_cap,0)
    h_temp,w_temp= frame0.shape # We will use this to reconstruct 
                                # images after we divide it for temporal
                                # searching
    h_temp= int(np.ceil(h_temp/temp_size))
    w_temp = int(np.ceil(w_temp/temp_size))

    h_space,w_space= frame0.shape # We will use this to reconstruct 
                                # images after we divide it for temporal
                                # searching
    h_space= int(np.ceil(h_space/jpeg_size))
    w_space = int(np.ceil(w_space/jpeg_size))

    for i in range(0,int(frame_count)):
        cframe = capture_frame(video_cap,i)
        if i==0:    
            cur_frames= divider.encoder(cframe)
            Fn_current = divider.decoder(cur_frames,h_temp,w_temp)
            predicted = None
        
        else: 
            motion_Vec= motion_estimate(cframe,Fn_1_constructed,temp_size,search_space)
            predicted= compensator(motion_Vec,Fn_1_constructed,temp_size,h_temp,w_temp)   
            Fn_current= cframe - predicted

        compressed_p = jpeg.compress(Fn_current)
        compressed.extend(compressed_p)
        Fn_1_constructed= jpeg.decompress(compressed_p,h_space,w_space)
        if predicted is not None : Fn_1_constructed+= predicted
                ########
        # Entropy Encoding
        ####
        # first let's add the headers and vectors 
        #  main idea is to have each block as following 
        compressed.append("#")
        if predicted is not None:
            motion_Vec_flattened = []
            print("*********************************")
            #print(motion_Vec)
            for u in range(h_temp):
                for v in range(w_temp): 
                    motion_Vec_flattened.extend(list(motion_Vec[(u,v)]))
                    
            compressed.extend(motion_Vec_flattened)    
        compressed.append("#")
        if i == 30:
            break
    return compressed,h_space,w_space,h_temp,w_temp


def video_decompress(video_list,rows,cols,rt,ct,temp_size=64,jpeg_size=8,compression_type=0):

    frame_idx= 0
    motion_idx= 0
    end_motion_idx=0

    jpeg= JPEG(jpeg_size,compression_type)
    counter=0
    while frame_idx < len(video_list):
        motion_idx= video_list.index('#',frame_idx)
        end_motion_idx =  video_list.index('#',motion_idx+1)
        if end_motion_idx-1 == motion_idx: # means this frame is a ref 
            # I want to do jpeg alone
            Fn_1_reconstructed= jpeg.decompress(video_list[frame_idx:motion_idx],rows,cols)

        else: 
            Dn = jpeg.decompress(video_list[frame_idx:motion_idx],rows,cols)
            motion_vec = video_list[motion_idx+1:end_motion_idx] # this is a list an we works on a dict
            motion_vec =get_motion_vetor(motion_vec,rt,ct )
            predicted= compensator( motion_vec,Fn_1_reconstructed,temp_size,rt,ct)
            Fn_1_reconstructed = predicted+ Dn


        cv2.imwrite(f"frame {counter}.jpg",Fn_1_reconstructed)
        counter+=1
        frame_idx = end_motion_idx+1



video_comp,r,c ,rt,ct= video_compression("quit.mp4",16,5,8,0)
video_decompress(video_comp,r,c,rt,ct,16)

