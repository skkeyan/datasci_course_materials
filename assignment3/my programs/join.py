import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    table_name = record[0]  # Table name - Order or Lineitem
    key = record [1]        # Order ID in both the Order and Lineitem records
    attributes = record[0:] # Get all the attributes
    mr.emit_intermediate(key, attributes)

def reducer(key, list_of_values):
    # key: Order ID
    # list_of_values: list of 1 Order record plus all line-item records

    order_record = list_of_values[0]  # First Item in the list is the order record
        
    for i in xrange(1,len(list_of_values)):  # Loop through all the other records which are line-item records
        line_item_record = list_of_values[i]
        join_record = order_record + line_item_record
        #print join_record
        mr.emit(join_record)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
