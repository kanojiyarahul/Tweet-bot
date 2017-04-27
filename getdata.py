__author__ = 'rahul kanojiya'
from bs4 import BeautifulSoup
import re
import requests;
contests = []
def run():
    #url = "C://Users/rahul kanojiya/PycharmProjects/Project1/htmldata.html"
     # soup = BeautifulSoup(open(url,encoding="utf8").read() ,"html5lib")
    url = "http://clist.by/";
    raw_data = requests.get(url);
    soup = BeautifulSoup(raw_data.content,'html5lib');

    div = soup.find_all("div" ,attrs = {"class" : re.compile("contest running")})

    for item in div:
        di ={}
        lis = item.find_all("a" ,title = True)
        di['event'] = lis[0].string
        di['link'] = lis[0]['href']
        str = item.div.div.a.string
        str = str.strip(' \t\n\r')
        di['start-time'] = str

        str2 =item.div.div.next_sibling.next_sibling.string
        str2 = str2.strip('\t\r\n')
        di['duration'] = str2
        contests.append(di)




