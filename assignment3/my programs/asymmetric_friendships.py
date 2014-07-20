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
    
    friend_list =[friend,1]
    mr.emit_intermediate(person,friend_list)
    
    not_friend_list = [person,-1]
    mr.emit_intermediate(friend,not_friend_list)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    
    person = key  # Person for whom the relationships are evaluated
    friendship_list = list_of_values

    score = {} #initialize an empty dictionary
    
    for friend,val in friendship_list:
        score[friend] = score.get(friend,0) + val
    
    score_tuple = score.items()
    count = 0
    
    for friend,val in score_tuple:
        if (val != 0): 
            asymmetric_list = [person,friend]
            count = count + 1
            mr.emit(tuple(asymmetric_list))
            #asymmetric_list = [friend,person]
            #mr.emit(asymmetric_list)
    
    #print count
    
# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
