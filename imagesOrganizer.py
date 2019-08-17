
import os,sys
import datetime

def similarGroup(dr):

    onlyDrs = list(filter(lambda x:os.path.isdir(x),os.listdir()))

    lastModified = sorted(onlyDrs,key=lambda x:os.stat(x).st_mtime)[-1]

    print(lastModified)

    os.chdir("/home/ipcamftp/ftp/IPCAM")
    os.system("sudo python3 similarGroup.py "+dr+"/"+lastModified)

def main():
    if len(sys.argv) > 1:
        dateFolder = sys.argv[1]
    else:
        dateFolder = str(datetime.date.today()).replace("-",'')

    finalDir = "photos/"+dateFolder+"/images"
    os.chdir(finalDir)
    files = os.listdir()

    onlyFiles = list(filter(lambda x:os.path.isfile(x),files))
    print(len(onlyFiles),len(files))
    if len(files) == len(onlyFiles):
        try:
            for i in range(0,24):
                os.mkdir(str(i).zfill(2))
        except Exception:
            k=0

    for fl in onlyFiles:
        hr=str(fl[7:].split(".")[0][:2])
        os.system("mv "+fl+" "+hr+"/")


    similarGroup(finalDir)


if __name__ == "__main__":
    main()
