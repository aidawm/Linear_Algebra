import numpy as np 

free_columns = []
pivot_points = []

def interchange(matrix , row1 , row2):
    
    matrix[[row1,row2]] = matrix[[row2,row1]]

def replacement(matrix,pivot_point,selected_row):
    
    pivot_value = matrix[pivot_point[0],pivot_point[1]]
    selected_value = matrix[selected_row,pivot_point[1]]
    if(selected_value == 0):
        return 
    
    matrix[selected_row,:] = matrix[selected_row,:]*pivot_value-matrix[pivot_point[0],:]*selected_value
    
def scaling(matrix,selected_point):
    
    selected_value = matrix[selected_point[0],selected_point[1]]
    
    matrix[selected_point[0],:] = matrix[selected_point[0],:]/selected_value

def find_pivot_column(matrix,row,current_column):
    col = matrix[:,current_column]
    while(col[row]==0):
        f =0 
        for i in range(row+1,len(col),1): 
            if (col[i]!=0):
                interchange(matrix,row,i)
                f=1
                break
        if(f==0):
            
            if(current_column == matrix.shape[1]-1):
                current_column +=1
                return current_column
            
            free_columns.append(current_column)
            current_column+=1
            
    
            col = matrix[:,current_column]
    
    pivot_points.append((row,current_column))
    
    return current_column

def make_matrix_to_echelon_form(matrix):
    
    r,c = matrix.shape
    current_column =0
    for i in range(r):
        col = matrix[:,current_column]
        current_column= find_pivot_column(matrix,i,current_column)
        
        if current_column == c :
            break
        
        for j in range (i+1,r,1):
            replacement(matrix,(i,current_column),j)
        
        current_column+=1

def make_matrix_to_reduced_echlon_form(matrix):
    make_matrix_to_echelon_form(matrix)
    for p in pivot_points:
        if (p[1]>=matrix.shape[1]):
            continue
        scaling(matrix,p)
        
        r,c = p
        
        for i in range(r-1,-1,-1):
            replacement(matrix,p,i)
    
    
