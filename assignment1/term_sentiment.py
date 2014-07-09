import json
import sys

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    
    for line in tweet_file:
        each_tweet_string = json.loads(line)
        #print type(each_tweet_string)
        try:
            tweet_text_as_is = each_tweet_string["text"]
            tweet_text = tweet_text_as_is.encode('utf-8')
            tweet_text = tweet_text.rstrip()
            words_in_tweet = tweet_text.split()
            #print words_in_tweet
        except:
            continue
        
    #tweet_text = "Listening to glee because glee songs are the best shizzle around this place well not the best but I love them okay"
    #tweet_text = "Doing homework bored bored bored bored so much i might have an overload mad the netball team thougghhh"
        
        value_tweet = 0
        count = 0
        average_score = 0
        for word in words_in_tweet:
            word = word.lower()
            if word not in scores:
                #print word
                #print "Not in dictionary"
                scores[word]=0
                #print scores[word]
                value_tweet = value_tweet + 0
            else:
                #print word
                #print "In Dictionary"
                #print scores[word]
                value_tweet = value_tweet + scores[word]
                count = count + 1
        #print value_tweet
        #print count
    
        if count == 0:
            average_score = 0
        else:
            average_score = float(value_tweet) / float(count)
    
        #print average_score
    
        for word in words_in_tweet:
            word = word.lower()
            if scores[word] == 0:
                scores[word] = average_score
            else: continue
    
    word_score_tuple = scores.items()
    
    for key,val in word_score_tuple:
        if key.isalpha():
               print key.encode('utf-8'),val

    
if __name__ == '__main__':
    main()
