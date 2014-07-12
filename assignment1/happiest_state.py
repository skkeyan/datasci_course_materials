import json
import sys

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
 
    # Latitude, Longitude for US States
    state_coord_dict = dict()
        
    state_coord_dict["AK"] = [61.385,-152.26]
    state_coord_dict["AL"] = [32.799,-86.8]
    state_coord_dict["AR"] = [34.9513,-92.38]
    state_coord_dict["AS"] = [14.24,-170.72]
    state_coord_dict["AZ"] = [33.771,-111.38]
    state_coord_dict["CA"] = [36.17,-119.74]
    state_coord_dict["CO"] = [39.0646,-105.3272]
    state_coord_dict["CT"] = [41.5834,-72.7622]
    state_coord_dict["DC"] = [38.8964,-77.0262]
    state_coord_dict["DE"] = [39.3498,-75.5148]
    state_coord_dict["FL"] = [27.8333,-81.717]
    state_coord_dict["GA"] = [32.9866,-83.6487]
    state_coord_dict["HI"] = [21.1098,-157.5311]
    state_coord_dict["IA"] = [42.0046,-93.2140]
    state_coord_dict["ID"] = [44.2394,-114.5103]
    state_coord_dict["IL"] = [40.3363,-89.0022]
    state_coord_dict["IN"] = [39.8647,-86.2604]
    state_coord_dict["KS"] = [38.5111,-96.8005]
    state_coord_dict["KY"] = [37.6690,-84.6514]
    state_coord_dict["LA"] = [31.1801,-91.8749]
    state_coord_dict["MA"] = [42.2373,-71.5314]
    state_coord_dict["MD"] = [39.0724,-76.7902]
    state_coord_dict["ME"] = [44.6074,-69.3977]
    state_coord_dict["MI"] = [43.3504,-84.5603]
    state_coord_dict["MN"] = [45.7326,-93.9196]
    state_coord_dict["MO"] = [38.4623,-92.3020]
    state_coord_dict["MP"] = [14.8058,145.5505]
    state_coord_dict["MS"] = [32.7673,-89.6812]
    state_coord_dict["MT"] = [46.9048,-110.3261]
    state_coord_dict["NC"] = [35.6411,-79.8431]
    state_coord_dict["ND"] = [47.5362,-99.7930]
    state_coord_dict["NE"] = [41.1289,-98.2883]
    state_coord_dict["NH"] = [43.4108,-71.5653]
    state_coord_dict["NJ"] = [40.314,-74.5089]
    state_coord_dict["NM"] = [34.8375,-106.2371]
    state_coord_dict["NV"] = [38.4199,-117.1219]
    state_coord_dict["NY"] = [42.1497,-74.9384]
    state_coord_dict["OH"] = [40.3736,-82.7755]
    state_coord_dict["OK"] = [35.5376,-96.9247]
    state_coord_dict["OR"] = [44.5672,-122.1269]
    state_coord_dict["PA"] = [40.5773,-77.264]
    state_coord_dict["PR"] = [18.2766,-66.3350]
    state_coord_dict["RI"] = [41.6772,-71.5101]
    state_coord_dict["SC"] = [33.8191,-80.9066]
    state_coord_dict["SD"] = [44.2853,-99.4632]
    state_coord_dict["TN"] = [35.7449,-86.7489]
    state_coord_dict["TX"] = [31.106,-97.6475]
    state_coord_dict["UT"] = [40.1135,-111.8535]
    state_coord_dict["VA"] = [37.768,-78.2057]
    
    state_coord_dict["VI"] = [18.0001,-64.8199]
    state_coord_dict["VT"] = [44.0407,-72.7093]
    state_coord_dict["WA"] = [47.3917,-121.5708]
    state_coord_dict["WI"] = [44.2563,-89.6385]
    state_coord_dict["WV"] = [38.4680,-80.9696]
    state_coord_dict["WY"] = [42.7475,-107.2085]
    
    # Dictionary to store the average sentiment score of state
    
    state_total_senti_score = dict()
    state_total_num_times = dict()
    state_avg_senti_score = dict()
     
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    for line in tweet_file:
        each_tweet_string = json.loads(line)
        
        #print each_tweet_string.keys()
              
        try:
            tweet_coordinates = each_tweet_string["coordinates"]
            tweet_place = each_tweet_string["place"]
                       
            if len(tweet_coordinates) > 0: 
                country_code = tweet_place["country_code"]
                if country_code == "US": 
                    tweet_coord = tweet_coordinates["coordinates"]
                    longitude_tweet = tweet_coord[0]
                    latitude_tweet = tweet_coord[1]
                    #print latitude_tweet,longitude_tweet
            
                    tweet_text_as_is = each_tweet_string["text"]
                    tweet_text = tweet_text_as_is.encode('utf-8')
                    words_in_tweet = tweet_text.split()
            
                    value_tweet = 0
                    for word in words_in_tweet:
                        word = word.lower()
                        if word not in scores:
                            value_tweet = value_tweet + 0
                        else:
                            value_tweet = value_tweet + scores[word]
                    #print value_tweet
                    
            
                    for key,val in state_coord_dict.items():
                        if ((abs(longitude_tweet - val[1]) < 0.5) & (abs(latitude_tweet - val[0]) < 0.5)):
                            #print key,value_tweet
                            state_total_senti_score[key] = state_total_senti_score.get(key,0) + value_tweet
                        elif ((abs(longitude_tweet - val[1]) < 1) & (abs(latitude_tweet - val[0]) < 1)):
                            #print key,value_tweet
                            state_total_senti_score[key] = state_total_senti_score.get(key,0) + value_tweet
                        elif ((abs(longitude_tweet - val[1]) < 1.5) & (abs(latitude_tweet - val[0]) < 1.5)):
                            #print key,value_tweet
                            state_total_senti_score[key] = state_total_senti_score.get(key,0) + value_tweet
                        elif ((abs(longitude_tweet - val[1]) < 2) & (abs(latitude_tweet - val[0]) < 2)):
                            #print key,value_tweet
                            state_total_senti_score[key] = state_total_senti_score.get(key,0) + value_tweet
                        else:
                            #print key,value_tweet
                            state_total_senti_score["NY"] = state_total_senti_score.get("NY",0) + value_tweet    #the default state
                        state_total_num_times[key] = state_total_num_times.get(key,0) + 1
        except:
            continue
    
    
    
    state_score_tuple = state_total_senti_score.items()
    state_score_avg = list()
    
    for key,val in state_score_tuple:
        if key.isalpha():
            val = (float(val) / float(state_total_num_times[key]))
            state_score_avg.append((val,key))
            #print key.encode('utf-8'),)
    
    state_score_avg.sort(reverse=True)
    
    iteration = 0
    for val,key in state_score_avg:
        if iteration < 1: 
            print key.encode('utf-8')
            iteration = iteration + 1
        else: break
 

if __name__ == '__main__':
    main()
