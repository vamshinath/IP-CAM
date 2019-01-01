from os import system as call
from time import sleep as wait
import datetime,re
#call("python3 -m http.server 8000 &")

counter = 0
while True:
	wait(30)
	dt = re.sub("-","",str(datetime.date.today()))
	call("python3 getPics.py")
	counter+=1
	print("delay 30 sec")
	print("counter:"+str(counter))
	wait(30)
	if counter > 3 :
		if counter % 4 == 0:
			call('find '+dt+' -type f -name "*.jpg" ! -empty -exec mv {} "saved/'+dt+'"  \;')

		if counter % 8 == 0:
			call("python3 similarGroup.py saved/"+dt)
			call("python3 get_vid.py")
			call("python3 h264Sticher.py")
			counter=0
