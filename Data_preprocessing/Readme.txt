File Name: "Sachsenhausen_shapefile_vehiclecount distribution_zones description" consists of a prototype of shapefile map with the vehicle count on each of the edges for all the 
three streets (Mörfelder Landstrasse, Kennedyallee,Darmstädter).
This was done to anaylse the flow of vehicle and also to assign the zones (origin and destination). As section based modelling was performed each section is also shown in detail in this file.
This file was used to create attraction production matrix which can be seen in the file "OD Matrix Estimation_Gravity Model".

File Name: "OD Matrix Estimation_Gravity Model" This file contains the process to create OD Matrix file for each of the streets. This file contains 7 OD matrix  which are created 
using gravity model and 
sample process. The OD matrix generated using gravity model is then used as an input for python script so that the matrix balancing approach cpuld be applied to have a proper OD
 matrix file for each of the streets.

File Name: Darmstaedter_1,Darmstaedter_2,Kennedyallee_1,Kennedyallee_2,Moerfelder_Ldstr_1,Moerfelder_Ldstr_2,Moerfelder_Ldstr_3 contains the OD matrix output generated in the file
 OD Matrix Estimation_Gravity Model
The python script "ODME_estimation" is run one by one and read all the files containing OD matrix and then apply matrix balancing approach and generate output (Balanced OD Matrix)
 in the folder Matrix_Balancing_Approach_Output.
Please make sure to change the filename in the python script before running the python script.

Folder Induction Loop Data contains all the file used for generating normalized share with 15 minute interval which is used to distribute the vehicle count.
File "01_Moerfelder-Ldstr_FR-N" is applied to vehicle travelling to east(Darmstädter Landstrasse) using Mörfelder Landstrasse
File "01_Moerfelder-Ldstr_FR-N" is applied to vehicle travelling on Kennedyallee towards North(into the city)
File "14_Friedensbruecke_FR-S" is applied to vehicle travelling towards South on Kennedyallee
File "09_Ignatz-Bubis-Bruecke_FR-S" is applied to vehicle travelling on Darmstädter Landstrasse towards South(Babahnaeuser-Ldstr)
File "09_Ignatz-Bubis-Bruecke_FR-S" is applied to vehicle travelling on Mörfelder Landstrasse towards west(Kennedyallee)
File "03_04 Darmstaedter-Ldstr" is applied to vehicle travelling on Darmstädter Landstrasse towards North(into the city)





