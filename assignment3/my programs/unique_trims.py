import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence id identifier
    # value: nucleotide contents
    sequence_id = record[0]
    nucleotide = record[1]
    #print len(nucleotide)
    trimmed_nucleotide = nucleotide[0:(len(nucleotide)-10)]
    
    mr.emit_intermediate(trimmed_nucleotide,1)

def reducer(key, list_of_values):
    # key: Trimmed nucleotide
    # value: list of occurrence counts
    
    mr.emit(key)  # key is the nucleotide

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
