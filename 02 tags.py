import requests
from bs4 import BeautifulSoup
def getdata(path):
    with open(path,"r") as f:
        hmtl_doc=f.read()
    soup=BeautifulSoup(hmtl_doc,'html.parser')
    #print(soup.title.string)
    with open("data/dimple1.text","a") as d:
        d.write(soup.title.string)
        d.write(soup.p.string)
        d.write(soup.div.string)
getdata("sample.html")

 