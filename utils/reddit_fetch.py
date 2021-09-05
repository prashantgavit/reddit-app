import requests
import json
import datetime
import pandas as pd
import time

def get_reddit_data(start_date,end_date,sub_reddit):
    start_date = str(datetime.datetime.strptime(start_date, '%Y-%m-%d').timestamp()).split('.')[0]
    # page_creation_date = '1369920198'
    end_date = str(datetime.datetime.strptime(end_date, '%Y-%m-%d').timestamp()).split('.')[0]
    url = f'https://api.pushshift.io/reddit/search/submission/?subreddit={sub_reddit}&before={end_date}'
    data = []
    while (int(end_date) > int(start_date)):
        response = requests.get(url)
        data = data + response.json()['data']
        end_date = str(response.json()['data'][-1]['created_utc'])
        url = f'https://api.pushshift.io/reddit/search/submission/?subreddit={sub_reddit}&before={end_date}'
    pd_data = pd.DataFrame(data)
    return pd_data

if __name__ == '__main__':
    get_reddit_data('2021-01-01','2021-01-31','Unclejokes')
