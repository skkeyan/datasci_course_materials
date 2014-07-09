import json
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    #print type(tweet_file)
    hash_dict = dict() # Create a dictionary to hold the hashtag and number of occurrences
    
    for line in tweet_file:
        each_tweet_string = json.loads(line)
        #print type(each_tweet_string)
        #print each_tweet_string.keys()
        try:
            tweet_entities = each_tweet_string["entities"]   #This is a dictionary
            tweet_hashtag = tweet_entities["hashtags"]       #This is a list
        except:
            continue
        
        for word in tweet_hashtag:  #word is a dictionary
            hash_text_as_is = word["text"]
            if hash_text_as_is.isalpha(): hash_text = hash_text_as_is.encode('utf-8')
            else: continue
            
            hash_dict[hash_text] = hash_dict.get(hash_text,0) + 1 #Building hashtag dictionary
            #print hash_text
            #print type(hash_text)
    
    hash_score_tuple = hash_dict.items()
    hash_score_tuple_reverse = list()
    
    for key,val in hash_score_tuple:
        if key.isalpha():
            hash_score_tuple_reverse.append((val,key))
    
    hash_score_tuple_reverse.sort(reverse=True)
    
    iteration = 0
    for val,key in hash_score_tuple_reverse:
        if iteration < 10: 
            print key.encode('utf-8'),val
            iteration = iteration + 1
        else: break

     

if __name__ == '__main__':
    main()