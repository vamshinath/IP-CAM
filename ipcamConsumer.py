from flask import Flask, render_template,request,redirect,url_for,Markup
app = Flask(__name__)
import os

def getImagesFromDir(dt,tm):
    dr = "/home/ipcamftp/ftp/IPCAM/photos/"+dt+"/images/"+tm+"/"
    imgs=os.listdir(dr)
    return imgs

@app.route("/mainpage",methods=["POST","GET"])
def mainpage():
    idate = request.form.get("date").replace("-","")
    itime = request.form.get("time").split(":")[0]
    print(idate,itime)

    images=getImagesFromDir(idate,itime)

    return render_template('images.html',date=idate,images=images,tm=itime)

@app.route("/")
def ma():
    return render_template("index.html")

if __name__ == '__main__':
    app.run('0.0.0.0',port=8001)

#
