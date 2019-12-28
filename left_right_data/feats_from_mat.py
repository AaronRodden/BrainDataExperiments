import pandas as pd
import numpy as np
import scipy.io as sio
import os

def create_feat_batch(matfile):
    matLeft = sio.loadmat(matfile)['eeg']['imagery_left']
    matRight = sio.loadmat(matfile)['eeg']['imagery_right']
    unpackedL = matLeft[0][0]
    unpackedR = matRight[0][0]
#    print(unpackedL)
#    dictL = {}
#    dictR = {}
#    features = {}
#    features = []
    eegL = [col[:358400] for col in unpackedL]
#    eegL = eegL[358400:]
#    print(len(eegL))
#    for row in eegL:
#        if len(row) != 358400:
#            print("Problem with file " + matfile)
#            print(len(row))
    directionL = [0] * len(unpackedL)
    df_left = pd.DataFrame()
    df_left['eeg'] = eegL
    df_left['direction'] = directionL
#    print(df_left)
    eegR = [col[:358400] for col in unpackedR]
#    eegR = eegR[358400:]    
#    print(len(eegR))
    directionR = [1] * len(unpackedR)
    df_right = pd.DataFrame()
    df_right['eeg'] = eegR
    df_right['direction'] = directionR
    
    df_all = df_left.append(df_right)
    
#    print(df_all)
#    features = Merge(dictL,dictR)
#    features = features.append(dictL)
#    features = features.append(dictR)
#    for featIndex in range(0,len(unpackedL)):
#        leftFeats = unpackedL[featIndex]
#        leftFeats = leftFeats[:358400]
#        rightFeats = unpackedR[featIndex]
#        rightFeats = rightFeats[:358400]
#        features.append([0,leftFeats])
#        features.append([1,rightFeats])
    
#    print(features)
#    print(features[0][1])
#    return features
#    print(dictL)
#    return dictL, dictR
    return df_all


def get_feats_from_mat(data_dir):
#    DATA_DIR = "data"    
#    final_feats = []
#    final_left = []
#    final_right = []
    final_df = pd.DataFrame()
    for file in os.listdir(data_dir):
         filename = os.fsdecode(file)
         if filename.endswith(".mat"): 
             path = os.path.join(data_dir, filename)
#             final_feats.extend(create_feat_batch(path))
#             newL, newR = create_feat_batch(path)
#             final_left.append(newL)
#             final_right.append(newR)
             new_df = create_feat_batch(path)
#             print(new_df)
             final_df = final_df.append(new_df)

#    print(final_df)
#    print(final_left)
#    return final_feats
#    return final_left,final_right
    return final_df

if __name__ == "__main__":
    pass
#    DATA_DIR = "data\\train"
#    get_feats_from_mat(DATA_DIR)
    create_feat_batch("data\\train\\s01.mat")
    
    

