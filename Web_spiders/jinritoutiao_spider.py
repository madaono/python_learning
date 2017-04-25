# coding：utf-8
import requests
import json
import time

def getData():
    url = 'http://www.365yg.com/api/pc/feed/?category=video&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true'
    fData = requests.get(url).text

    tData = json.loads(fData)
    news = tData['data']
    allData = {}
    # print(news)
    for i in news:
        if(i['has_video'] == True):
            allData[i['title']]=i['source_url']
            # if(i['comments_count']):
            #     print(i['comments_count'])

    print(allData)

def timer1():
    while True:
        time.sleep(3)
        getData()

timer1()