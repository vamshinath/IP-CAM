import subprocess,os,time

os.chdir("photos")
subprocess.Popen(["python3", "-m","http.server"])

while True:

	dirs = os.listdir()

	dirs = list(map(int,dirs))

	dirs.sort()

	ct = len(dirs)

	if ct > 15:
		rmd=dirs[0]
		subprocess.Popen(["rm","-rf",str(rmd)])

	time.sleep(3600*12)

