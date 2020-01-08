import json

from urllib.request import urlopen

from selenium import webdriver

import time

def look_for_new_video():
    api_key = 'AIzaSyD3xSFdOJTAu29FlCmaKxTrVIzMPfGbzMY'
    channel_id = 'UCR6yfDK_u5EXby7CnG9-rYw'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search'

    url = base_search_url+'key={}&channelid={}&part=snippet,id&order=date&maxResults=1'.format(api_key, channel_id)
    inp = urlopen(url)
    resp = json.load(inp)

    vidID = resp['items'][0]['id']['videoId']

    video_exists = False
    with open('videoId.json', 'r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != vidID:
            driver = webdriver.Firefox()
            driver.get(base_video_url+vidID)
            video_exists = True


    if video_exists:
        with open('videoId.json', 'w') as json_file:
            data = {'videoId': vidID}
            json.dump(data, json_file)

try:
    while True:
        look_for_new_video()
        time.sleep(10)
except KeyboardInterrupt:
    print('stopping')