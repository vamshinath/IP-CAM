import os,time
import datetime,re,pytz

path="../photos/"+re.sub("-","",str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))).split()[0]+"/images/vids"
os.chdir(path)
files=os.listdir('.')

tmp =[]
for fl in files:
    if ".264" in fl:
        tmp.append(fl)

files=sorted(tmp)

tmnow=re.sub("-","",str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))).split()[0]
dst=open(tmnow+".264","wb")
for x in files:
    tmp=open(x,'rb')
    dst.write(tmp.read())
    tmp.close()
    os.system("/home/vamshi/IPCAM/IP-CAM/a.out "+x)
    os.remove(x)
dst.close()
os.system("/home/vamshi/IPCAM/IP-CAM/a.out "+tmnow+".264")
print("videos Combined!")
