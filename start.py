from os import system as call
from time import sleep as wait
import datetime,re
import pytz

#call("python3 -m http.server 8000 &")

counter = 0
while True:
	dt=re.sub("-","",str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))).split()[0]
	print(dt)
	call("python3 similarGroup.py ../photos/"+dt+"/images/")
	call("python3 get_vid.py")
	call("python3 h264Sticher.py")
	call("mkdir -p scanned/"+dt)
	call("find ../photos/"+dt+"/images/* -name '*.jpg' -exec mv {} ./scanned/"+dt+" \;")
	call("python3 similarGroup.py ./scanned/"+dt+" &")
	wait(180)
