from copy import copy
from turtle import clear
from urllib import response
from cgitb import html
from re import search
import requests
from bs4 import BeautifulSoup as bs




setvar=set()

def details():
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
                setvar.add(fullstring)
                
            else:
                # print("not found")
                pass
    # for i in setvar:
    #     print (i)

details()


# list1=[]
# a=set(list1)

