# coding：utf-8
import requests
import json
import time


def getData():
    url = 'https://m.toutiao.com/list/?tag=video&ac=wap&count=20&format=json_raw&as=A1B5E8EF591BDC3&cp=58F92BED3CE33E1&min_behot_time='+ str(int(time.time()))
    fData = requests.get(url).text
    # print(fData)
    tData = json.loads(fData)
    # print(tData)
    news = tData['data']
    print(news)
    allData = {}
    # print(news)
    # for i in news:
    #     if(i['display_url'] != ''):
    #         allData[i['title']]=i['display_url']
    #         # if(i['comments_count']):
    #         #     print(i['comments_count'])
    # print(allData)

def timer1():
    while True:
        time.sleep(3)
        getData()

timer1()