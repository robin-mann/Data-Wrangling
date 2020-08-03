"""
Created on Thu May 28 11:02:39 2020

@author: Robin Mann

This code coverts data in horizontally-repeating blocks of 256 columns into one
block of 256 columns by vertically appending the blocks.

This version of the programm uses a pandas dataframe and lists of lists to accomplish the goal.

input data file: my_practice_csv.csv

output data file: my_OUTPUT_csv.csv

"""


import pandas as pd

def initialize_LOL(thisLOL,numSubLists):
    
    for i in range(numSubLists):
        thisLOL.append([])
   
def printVert(thisList):
    #prints the elements of a list vertically
    for element in thisList:
        print(element)


def printV2(thisLOL):
    #prints the subslists of thisLOL vertically, side-by-side
    for i in range(len(thisLOL[0])):
     
        output_str = ""
        for k in range(finalColNum):
            output_str += str(thisLOL[k][i])+ "    "
        print(output_str)    
        
        
        
def convertToByRow(thisLOL):
    #converts a list of column-lists to a list of row-lists
    
    retList = []
    for i in range(len(thisLOL[0])):
     
        outputList = []
        
        for k in range(finalColNum):
           
            outputList.append(thisLOL[k][i])        
        retList.append(outputList)
           
    return(retList)
    
 #-------------------------------------------------------------------   


#Read the file into a dataframe
df = pd.read_csv('my_practice_csv.csv', header = None)
print(df)

# initializations

finalColNum = 256


num_rows = df.shape[0]
num_cols = df.shape[1]
LOLCols = []
initialize_LOL(LOLCols,finalColNum)



for i in range(num_cols):
    
    #strip the i-th column of data from df
    cList = list(df.iloc[0:num_rows,i])
    
    #determine which output column it gets added to        
    idx = i%finalColNum
       
    #add the column to the end of the correct output column
    LOLCols[idx].extend(cList)



#printV2(LOLCols)

LOLRows=convertToByRow(LOLCols)

myDataFrame = pd.DataFrame(LOLRows)

print(myDataFrame)   
   
myDataFrame.to_csv('my_OUTPUT_csv.csv', index=False, header=False)

    
   
    
    
    
    
    
    
    
    
    
    