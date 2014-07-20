import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: Tuple that identifies the target row & column number
    # value: value from the original matrix "a" and "b" that is required to be migrated to target cells
    matrix_name = record[0]
    row_no = record[1]
    col_no = record[2]
    cell_value = record[3]
    
    if matrix_name == 'a':
        for k in [0,1,2,3,4]:    # Dimensions of the matrix should be known before-hand and is hard-coded. In this case B is a 5*5 matrix
            key = (row_no,k)
            value = (col_no,cell_value)
            mr.emit_intermediate(key, value)
    else:
        for i in [0,1,2,3,4]:    # Dimensions of the matrix should be known before-hand and is hard-coded. In this case A is a 5*5 matrix
            key = (i,col_no)
            value = (row_no,cell_value)
            mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: (Row number, Column number) index of the target matrix
    # value: Values required to compute the target matrix cell value
    
    multiplied_value = {}  # Empty Dictionary - Holds the multiplied value
    num_times = {}    # Empty Dictionary - Needed to check whether A & B has values in the corresponding row & column no. since we are given sparse matrices
   
    for index,val in list_of_values:
        if (multiplied_value.has_key(index)):
            multiplied_value[index] = multiplied_value[index] * val
            num_times[index] = num_times[index] + 1
        else:
            multiplied_value[index] = val
            num_times[index] = 1
    
    multiplied_value_tuple = multiplied_value.items()
        
    matrix_cell_sum = 0  # To compute the sum across all multiplied items
    
    for key1,value1 in multiplied_value_tuple:
        if(num_times[key1] == 2):                         # Checking whether values exists both in A & B matrices in the corresponding locations
            matrix_cell_sum = matrix_cell_sum + value1
              
    output = list(key)                     # Building the output list - First include the key which is the row & column index
    output.append(matrix_cell_sum)         # Append the cell value for the corresponding row and column number
        
    mr.emit(tuple(output))                 # Send to Reducer

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
