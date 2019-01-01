from bs4 import BeautifulSoup
import requests,os,time,re
import urllib.parse
import datetime
from requests.auth import HTTPBasicAuth
from threading import Thread,active_count
authValue=HTTPBasicAuth('admin', 'vamshi81')

images=[]

def myrequest(url):
    return requests.get(url)

def download_img(url):

    #fname=url.split("/")[-1]
    if os.path.isfile(url[7:]):
        return
    try:
        data=myrequest(url)
        dfile=open(url[7:],"wb")
        for chunk in data.iter_content(chunk_size=1024):
            if chunk:
                dfile.write(chunk)
        dfile.close()
    except Exception as e:
        print(e)


def downloadDir(url,dr):
    global images
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
        images.append(url)







def downloadDirs(dirs):

    with open("lastvisited.txt",'r') as fl:
        for ln in fl:
            last=ln[:-1]

    #print(last)
    found=0
    for url,dr in dirs:
        if last == url:
            found =1

    if found == 0:
        last,_ = dirs[0]



    k=0
    for url,dr in dirs:
        if last != url and k == 0:
            continue
        k=1
        print("-----"+url)
        downloadDir(url,dr)
        with open("lastvisited.txt",'w') as fl:
            fl.write(url+"\n")




def downloadHelper(url):
    imgdirs=[]
    page = myrequest(url)

    if page.status_code != 200:
        print("page error"+str(page.status_code))
        return

    html = BeautifulSoup(page.text,"html.parser")

    table = html.find("table")

    trs = table.findAll('tr')[3:]
    for tr in trs:
        a=tr.find('td').find('a')
        if "images" in a.text:
            url=urllib.parse.urljoin(url,a.get('href'))
            imgdirs.append([url,a.text[:-1]])

    downloadDirs(imgdirs)



def main():

    global images
    images=[]
    dt = re.sub("-","",str(datetime.date.today()))
    print(dt)

    if dt == "":
        print("____URL mode_____")
        url = input("Enter imgs url:")
        name=input("enter foldername:")
        downloadDir(url,name)
    else:
        #os.chdir("192.168.1.101/sd")
        #if not os.path.isdir(dt):
        #    os.mkdir(dt)
        #os.chdir(dt)
        url = "http://admin:vamshi81@192.168.1.101/sd/"+dt
        downloadHelper(url)

        os.chdir("/home/vamshi/IP-CAM")

        with open(dt+".txt",'w') as fl:
            for img in images:
                fl.write(re.sub("://","://admin:vamshi81@",img)+"\n")
            # for img in images:
            #     Thread(target=download_img,args=(img,)).start()
            #     time.sleep(0.3)
        print("to finish.sh")
        os.system("sh finish.sh "+dt)








if __name__ == '__main__':
    main()
