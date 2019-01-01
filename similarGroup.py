#!/usr/bin/python3
# from tkinter import *
# from tkinter import filedialog
from skimage.measure import compare_ssim as ssim
import cv2
import os,shutil
import sys
import string,random,itertools,time
finaldir="SIMILAR/"
imgdata = {}
smctr=0
stm=0


def validFiles():
    fls=[]
    files =os.listdir()
    for fl in files:
        if os.stat(fl).st_size < 10000:
            continue
        fls.append(fl)
    return fls


def alert(msg,delay):
    global stm
    notify2.init("SimilarImages")
    msg=notify2.Notification("similarGroup",msg+"  "+str(round(time.time()-stm))+"sec","ficon.png")
    msg.set_timeout(delay*1000)
    msg.show()

def imgdatagen(path):
    global imgdata
    os.chdir(path)
    files=os.listdir()
    for fl in files:
        if os.path.isfile(fl):
            try:
                file_extension = os.path.splitext(fl)[1]
                if file_extension == ".jpg" or file_extension == ".png" or file_extension == ".JPG" or file_extension == ".PNG" :
                    imgdata[fl]=cv2.resize(cv2.cvtColor(cv2.imread(fl), cv2.COLOR_BGR2GRAY), (100, 100))
            except Exception:
                print("!")

def random_generator(size=2, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def compare(imgdata1,imgdata2,im1,im2):
    if imgdata1 is None or imgdata2 is None or not os.path.isfile(im1) or not os.path.isfile(im2):
        #alert("skiped !!",5)
        return
    global smctr
    global imgdata
    try:
        s = ssim(imgdata1, imgdata2)
        val=round(s*100,3)
        print(val)
        if val > 95:
            #imgdata.pop(im1)
            imgdata.pop(im2)
            newname=random_generator()
            smctr+=1
            #alert("Found similar:"+str(smctr),4)
            #shutil.copy(im1,finaldir+im1)
            #open(im2,'w').close()
            os.remove(im2)
    except Exception:
        print()


def scanner(path):
    global stm
    try:
        imgdatagen(path)
        global imgdata
        os.chdir(path)
        var=0
        files = validFiles()

        ttlcombi = len(files)
        print("no.of validFiles:"+str(ttlcombi))
        time.sleep(4)
        ttlcombi = ttlcombi*ttlcombi-1

        for fl,nxtfl in itertools.combinations(files,2):

            if os.path.isfile(fl) and os.path.isfile(nxtfl) :
                file_extension = os.path.splitext(fl)[1]
                file_extension2 = os.path.splitext(nxtfl)[1]
                if file_extension == ".jpg" :
                    if file_extension2 == ".jpg" :
                        compare(imgdata.get(fl),imgdata.get(nxtfl),fl,nxtfl)
                        var=var+1
                        print(str(var)+"/"+str(ttlcombi))

        #alert("SCAN FINISHED !!",10)
        print("\nFINISHED in: "+str(time.time()-stm))

    except Exception as arg:
        print(arg)

def main():
    global stm
    if len(sys.argv) != 2:
        print("Usage: python3 similarGroup.py dir_name")
        sys.exit()
    stm=time.time()
    path=os.getcwd()+"/"+sys.argv[1]
    for x in os.walk(path):
        scanner(x[0])
if __name__ == '__main__': main()
# root=Tk()
# root.geometry("350x350")
# label=Label(root,text="Path:")
# label.pack()
# b_start = Button(root, text="select Dir")
# b_start.place(relx=0.5, rely=0.5, anchor=CENTER)
# b_start['command']=scanner
# root.mainloop()
