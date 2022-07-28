
from copy import copy
from turtle import clear
from urllib import response
from cgitb import html
from re import search
import requests
from bs4 import BeautifulSoup as bs
import test
import time
a=set()
def rapid():
    
    base_url="https://msbte.org.in/"

    r= requests.get(base_url)
    htmlcontent=r.content

    soup=bs(htmlcontent,'html.parser')

    links=[]
    for ul in soup.findAll('ul',{'class':'sub-menu'}):
        for link in ul.findAll('a'):
            links.append(link.get('href'))


    keyword= ['result','Result','RESULT','Res','res','2022','summer','SUMMER','Summer','Sum','sum','.aspx','.html','.php']

    
    lst = links
    for i in lst:
        fullstring=str(i)
        for key in keyword:
            substring=str(key)
            if search(substring,fullstring):
                # print ("found")
                # print(fullstring)
                a.add(fullstring)
                
            else:
                # print("not found")
                pass
    print("------------------------------------------------------------")
    # for i in a:
    #     print (i)
    if a==test.setvar:
        print("no changes")

        def send_msg(text):
            token ="5207221766:AAGDKEpRrNWDDGMtOzFmfjsdKMk7SbhJyDQ"
            chatid="1213641848"
            url="https://api.telegram.org/bot"+token+"/sendMessage"+"?chat_id="+chatid+"&text="+text
            result=requests.get(url)
            print(result.json())

        send_msg("no changes")
    else:
        print ("false")

    
while True:
    rapid()
    time.sleep(10)




