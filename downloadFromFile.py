
import requests,os,time,re
import urllib.parse
import datetime
from requests.auth import HTTPBasicAuth

dt = re.sub("-","",str(datetime.date.today()))

authValue=HTTPBasicAuth('admin', 'vamshi81')

def myrequest(url):
    return requests.get(url,auth=authValue)


def download_img(url):

    #fname=url.split("/")[-1]
    if os.path.isfile(url.split("/")[-1]):
        return
    try:
        data=requests.get(url)
        dfile=open(url.split("/")[-1],"wb")
        for chunk in data.iter_content(chunk_size=1024):
            if chunk:
                dfile.write(chunk)
        dfile.close()
    except Exception as e:
        print(e)


flinks =[]
os.chdir(dt)
with open(dt+".txt",'r') as fl:
    for ln in fl:
        flinks.append(ln[:-1])

for url in flinks:
    print(url)
    download_img(url)
    time.sleep(3)
