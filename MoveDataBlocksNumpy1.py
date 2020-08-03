# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:53:43 2020

@author: Robin Mann



This code coverts data in horizontally-repeating blocks of 256 columns into one
block of 256 columns by vertically appending the blocks.

This version of the programm uses a pandas dataframe and numpy arrays to accomplish the goal.

input data file: my_practice_csv.csv

output data file: my_OUTPUT_csv.csv
"""


import numpy as np
import pandas as pd



def print2D(arr2D):
    
    rows = a.shape[0]
    cols = a.shape[1]
    
    for i in range(rows):
        output_str=''
        for j in range(cols):
            
            output_str += str(arr2D[i][j])+ '   '
        print(output_str)
        

#READ FILE into a dataframe
df = pd.read_csv('my_practice_csv.csv', header = None)
print(df)

a = df.to_numpy()
print (a)
print2D(a)
rows = a.shape[0]
cols = a.shape[1]
finalColNum = 256
Num_Blocks = int(cols/finalColNum)



#CREATE LIST of 2D array blocks to vertically stack
BlockList = []
start_col = 0;
end_before_col =finalColNum

for i in range(Num_Blocks):
    curr_block = a[0:rows, start_col:end_before_col]
    
    start_col +=finalColNum
    end_before_col +=finalColNum
    BlockList.append(curr_block)
    
    
#VERTICALLY STACK the blocks  
final_block = BlockList[0]

for i in range(Num_Blocks-1):
    final_block=np.vstack((final_block,BlockList[i+1]))
    
#print(final_block)    



#OUTPUT to file

myDataFrame = pd.DataFrame(final_block)

print(myDataFrame)   
   
myDataFrame.to_csv('numpy_output_csv.csv', index=False, header=False)

    