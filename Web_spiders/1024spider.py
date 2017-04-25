# -- coding: utf-8 --

import requests
import importlib
import sys
from bs4 import BeautifulSoup
import html5lib

importlib.reload(sys)

BaseUrl = "http://t66y.com/"
j=1

for i in range(1, 10):
  url = "http://t66y.com/thread0806.php?fid=22&search=&page="+ str(i)
  page = requests.get(url,  headers={'Accept-Encoding': 'identity'})
  soup = BeautifulSoup(page.text, "html5lib")
  print("reading page "+ str(i))
  counts = soup.find_all("td", class_="tal f10 y-style")

  for count in counts:
    if int(count.string)>15:                            #这里设置点击率的阈值
      videoContainer = count.previous_sibling.previous_sibling.previous_sibling.previous_sibling
      video = videoContainer.find("h3")
      print("Downloading link "+ str(j))
      line1 = (video.get_text())
      line2 = BaseUrl+video.a.get('href')
      line3 = "view **" + count.string + "** "
      print (line1)
      f = open('1024.md', 'a')
      f.write("\n"+"###"+" "+line1+"\n"+"<"+line2+">"+"\n"+line3+ "  "+ "page"+str(i)+"\n")
      f.close()
      j+=1