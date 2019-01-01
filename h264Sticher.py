import os,time
import datetime,re

path="saved/"+re.sub("-","",str(datetime.date.today()))+"/vids"
os.chdir(path)
files=os.listdir('.')

tmp =[]
for fl in files:
    if ".264" in fl:
        tmp.append(fl)

files=sorted(tmp)

tmnow=re.sub(':',"",str(datetime.datetime.time(datetime.datetime.now()))[:8])
dst=open(tmnow+".264","wb")
for x in files:
    tmp=open(x,'rb')
    dst.write(tmp.read())
    tmp.close()
    os.system("../../../a.out "+x)
    os.remove(x)
dst.close()
os.system("../../../a.out "+tmnow+".264")
print("videos Combined!")
time.sleep(150)
