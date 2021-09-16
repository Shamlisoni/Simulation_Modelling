#!/usr/bin/env python
#Script Name :  Traci_Traffic_light.py
#Creation Date: 29 August 2021
#Author: Shamli Soni
#Description: This scripts takes input as the OD matrix created using Gravity Model
                #and then uses the matrix balancing approach to balance the production and attraction
                #for each zones mentioned in the OD matrix.
                #Filename are hardcoded so need to changed as per requirement
                #all the output file are saved in the folder named as Matrix_Balancing_Approach_Output 

# import libraries
import numpy as np
import pandas as pd
import math
import csv

File_Name='Kennedyallee_1.xlsx'
# reads the OD matrix file (OD matrix input)
dataset = pd.read_excel((open(File_Name), 'rb'), index_col=0)
#dataset = pd.read_excel(r'File_Name',index_col=0)
#converts the data read into dataset
dataset_final1=dataset.to_numpy()
#extracts the last row of the dataset
last_row1=dataset_final1[-1]
#Changes the datatype of the last row
Col_Exp= last_row1[:-1].astype(int)

print("Last Row:",Col_Exp)
#extracts the last column of the dataset
last_col1=dataset_final1[:, -1]
#changes the datatype of the last column
Row_Exp= last_col1[:-1].astype(int)


print("Last Column:",Row_Exp)

#changes the datatype of the OD matrix from file to integer type
OD = dataset_final1[:-1, :-1].astype(int)
print("Dataset:",OD)
#calculates the sum of each rows and each columns in the OD matrix
Row_Total=OD.sum(axis=1)
Col_Total=OD.sum(axis=0)
#calculates the difference between the expected sum and calculated sum
Error_row = np.subtract(Row_Exp,Row_Total)
Error_col = np.subtract(Col_Exp,Col_Total)

#checks if the difference between the expected sum and calculated sum is zero or not if not zero then enters into the while loop
is_all_zero = np.all((Error_row == 0))
is_all_zero1 = np.all((Error_col == 0))
i=0

while (is_all_zero == False) or (is_all_zero1 == False)  :
    #iteration number
    i += 1
    print("i",i)
    #calculates the sum of each rows and each columns in the OD matrix
    Row_Total=OD.sum(axis=1)
    Col_Total=OD.sum(axis=0)
    print("Row_Total:",Row_Total)
    print("Col_Total:",Col_Total)
    #calculates the row factor used for balancing
    Row_Factor_tmp=np.divide(Row_Exp,Row_Total)
    Row_Factor_tmp1 = np.where(np.isnan(Row_Factor_tmp), 0, Row_Factor_tmp)[np.newaxis]
    Row_Factor=Row_Factor_tmp1.T
    print("Row_Factor:",Row_Factor_tmp1.T)
    print("Row_Factor:",Row_Factor.dtype)
    #calculates the column factor used for balancing
    Col_Factor_tmp=np.divide(Col_Exp,Col_Total)
    Col_Factor = np.where(np.isnan(Col_Factor_tmp), 0, Col_Factor_tmp)

    print("Col_Factor:",Col_Factor)
    print("Col_Factor:",Col_Factor.dtype)


    #Multiply the row factor and column factor to balance each of the cells in the OD matrix
    Final_matrix = Row_Factor * Col_Factor * OD
    Final_matrix1 = np.round(Final_matrix,2)
    OD = Final_matrix
    print("OD:",OD)

    #calculates the difference between the expected sum and calculated sum after matrix balancing approach
    Error_row1 = np.subtract(Row_Exp,Row_Total)
    Error_row = np.around(Error_row1)
    Error_row = Error_row.astype(int)
    print("Error_Col:",Error_row)
    Error_col1 = np.subtract(Col_Exp,Col_Total)
    Error_col = np.around(Error_col1)
    Error_col = Error_col.astype(int)
    print("Error_Row:",Error_col)

    
    is_all_zero = np.all((Error_row == 0))
    print("is_all_zero_row:",is_all_zero)
    is_all_zero1 = np.all((Error_col == 0))
    print("is_all_zero_col:",is_all_zero1)
    
    #if the difference is zero for expected sum and calculated sum for both rows and columns then exits the loop
else:
    print("Finally finished!")

    #writes the final file with the balanced OD matrix
with open('Matrix_Balancing_Approach_Output\Kennedyallee_1.csv', 'w', newline='') as file:
    mywriter = csv.writer(file, delimiter=',')
    mywriter.writerows(OD)
