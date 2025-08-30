#Defining the number of rows and columns
number_of_rows = 3
number_of_columns = 2

#INITIALIZING A MATRIX

#Initializing a matrix of 3 X 2  all zeros (Using list comprehension)
res = [ [0] * number_of_columns for i in range(number_of_rows)]
print(res)

#Initializing using a nested for loop
second_matrix=[]
for i in range(number_of_rows):
    row = []
    for j in range(number_of_columns):
        row.append(0)
    second_matrix.append(row)
   
print(second_matrix)

#Using * with deep copy
import copy
row = [0] * number_of_columns
res = [copy.deepcopy(row) for i in range(number_of_rows)]
print(res) 

#Declaring a matrix
arr = [[0] * number_of_columns] * number_of_rows
print(arr)

#Initializing using Numpy
import numpy as np
res1 = np.zeros((number_of_rows,number_of_columns) ,dtype= int)
print(res1)

#Looking up an index in the matrix
posMatrix= second_matrix[0][1]
print(posMatrix)

#Traversing a Matrix
arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(0,3): #Traversing rows
     for j in range(0,3): # Travering all columns
         print(arr[i][j])


#Checking for an element in the matrix
for i in range(0,3):
    for j in range(0,3):
        if(arr[i][j] == 6):
            print("YES FOUND")
        else:
            print("NO NOT FOUND")
