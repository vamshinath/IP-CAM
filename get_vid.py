from bs4 import BeautifulSoup
import requests,os,time,re
import urllib.parse
import datetime,pytz
from requests.auth import HTTPBasicAuth
vids=[]
authValue=HTTPBasicAuth('admin', 'vamshi81')

def myrequest(url):
    return requests.get(url,auth=authValue)

def downloadDirs(dirs):


    for url,dr in dirs:
        downloadDir(url,dr)


def downloadDir(url,dr):
    global vids
    print(dr,url)
    #if not os.path.isdir(dr):
    #    os.mkdir(dr)


    page = myrequest(url)
    if page.status_code != 200:
        print("page error"+str(page.status_code))
        return

    html = BeautifulSoup(page.text,"html.parser")
    table = html.find("table")

    trs = table.findAll('tr')[3:]

    for tr in trs:
        a=tr.find('td').find('a')
        url=urllib.parse.urljoin(url,a.get('href'))
        #download_img(url,dr)
        vids.append(url)


def downloadHelper(url):

    viddirs=[]
    page = myrequest(url)

    if page.status_code != 200:
        print("page error"+str(page.status_code))
        return

    html = BeautifulSoup(page.text,"html.parser")

    table = html.find("table")

    trs = table.findAll('tr')[3:]
    for tr in trs:
        a=tr.find('td').find('a')
        if "record" in a.text:
            url=urllib.parse.urljoin(url,a.get('href'))
            viddirs.append([url,a.text[:-1]])

    downloadDirs(viddirs)

def loadToList(fl):
	links = []

	try:
		with open(fl,'r') as fll:
			for ln in fll:
				links.append(ln[:-1])
	except Exception as e:
		k=0

	return links

def main():

    global vids
    dt=re.sub("-","",str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))).split()[0]
    os.chdir("../photos/"+dt+"/images/")

    files=sorted(os.listdir('.'))



    url = "http://192.168.0.111/sd/"+dt
    downloadHelper(url)

    mylist=set()

    visited=loadToList("visited.txt")

    for img in files:
        if img in visited:
            continue
        if not ".jpg" in img:
            continue
        img = int(img[7:11])
        for vid in vids:
            start,end=vid.split('/')[-1].split('_')[1:]
            start,end=int(start[:4]),int(end[:4])
            if img >= start and img <= end:
                mylist.add(vid)
                continue
            if img < start:
                break

    with open("visited.txt",'a') as fl:
        for img in files:
            fl.write(img+"\n")

    os.system("mkdir vids")
    os.chdir("vids")

    with open("tmp.txt",'w') as fl:
        for vid in mylist:
            fl.write(vid+"\n")

    os.system("wget -nc -i tmp.txt")


if __name__ == '__main__':
    main()
