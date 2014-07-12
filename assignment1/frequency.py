import json
import sys

def main():
    tweet_file = open(sys.argv[1])
    
    terms_dict = dict()
    terms_freq = dict()
    
    total_all_terms = 0.0
    
    for line in tweet_file:
        each_tweet_string = json.loads(line)
        try:
            tweet_text_as_is = each_tweet_string["text"]
            tweet_text = tweet_text_as_is.encode('utf-8')
            tweet_text = tweet_text.rstrip()
            words_in_tweet = tweet_text.split()
            #print words_in_tweet
        except:
            continue
        
        for word in words_in_tweet:
            if word.isalpha():
                word = word.lower()
                terms_dict[word] = terms_dict.get(word,1) + 1
                total_all_terms = total_all_terms + 1
            else: continue
        #print terms_dict
        #print count
    
    #print total_all_terms
    terms_tuple = terms_dict.items()
    
    for key,val in terms_tuple:
        terms_freq[key] = val / total_all_terms
    
    terms_freq_tuple = terms_freq.items()
    
    for key,val in terms_freq_tuple:
        if key.isalpha():
            print key.encode('utf-8'),val

    
if __name__ == '__main__':
    main()