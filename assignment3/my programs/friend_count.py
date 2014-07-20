import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person name
    # value: friend name
    person = record[0]
    friend = record[1]
    
    mr.emit_intermediate(person,friend)

def reducer(key, list_of_values):
    # key: person
    # list_of_values: list of friends
    total = 0
    for v in list_of_values:
      total += 1
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
