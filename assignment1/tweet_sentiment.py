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
    #print type(tweet_file)
    
    #afinnfile = open(sent_file)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    # print scores.items() # Print every (term, score) pair in the dictionary
    
    for line in tweet_file:
        each_tweet_string = json.loads(line)
        # print type(each_tweet_string)
        #print each_tweet.keys()
        try:
            tweet_text_as_is = each_tweet_string["text"]
            tweet_text = tweet_text_as_is.encode('utf-8')
            #tweet_text = "Listening to glee because glee songs are the best shizzle around this place well not the best but I love them okay"
            #tweet_text = "Doing homework bored bored bored bored so much i might have an overload mad the netball team thougghhh"
            words_in_tweet = tweet_text.split()
            #print words_in_tweet
        except:
            continue
        
        value_tweet = 0
        for word in words_in_tweet:
            word = word.lower()
            if word not in scores:
                #print word
                #print "Not in dictionary"
                value_tweet = value_tweet + 0
            else:
                #print "In Dictionary"
                #print scores[term]
                #print word
                #print scores[word]
                value_tweet = value_tweet + scores[word]
        print value_tweet        

if __name__ == '__main__':
    main()
