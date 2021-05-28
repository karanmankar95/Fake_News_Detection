import os
import json
from numpy.lib.function_base import append
import pandas as pd
rootdir = 'C://Users//manka//Documents//Predictive Analytics//Project//pheme-rnr-dataset//sydneysiege//rumours'
if 'non-rumours' in rootdir:
    labels = 0
elif 'rumours' in rootdir:
    labels = 1
column_names = ['id', 'news_url', 'title', 'no_of_retweets', 'label']
data = {}
df = pd.DataFrame(columns = column_names)

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if 'source-tweet' in subdir:
            try:
                id = file.split('.')[0]
                path = subdir+"//"+file
                f = open(path,'r')
                tweets_dict = json.loads(f.read())
                news_url = tweets_dict['user']['entities']['url']['urls'][0]['display_url']
                title= tweets_dict['text']
                no_of_retweets = tweets_dict['retweet_count']
                data = {'id' : id, 'news_url' : news_url, 'title' : title, 'no_of_retweets' : no_of_retweets, 'label' : labels}
                df = df.append(data, ignore_index='True')
            except:
                pass

df.to_csv(path_or_buf = rootdir+'.csv')
