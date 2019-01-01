import os,sys,time

def loadToList(fl):
	links = []

	try:
		with open(fl,'r') as fll:
			for ln in fll:
				links.append(ln[:-1])
	except Exception as e:
		k=0

	return links


def findUnique(nfl,ofl):

	downloaded = loadToList("downloaded.txt")

	newlinks=loadToList(nfl)
	oldlinks=loadToList(ofl)

	finallinks=[]

	for nl in newlinks:
		if not nl in oldlinks and not nl in downloaded:
			finallinks.append(nl)


	print("to download")
	print(len(finallinks))



	with open(nfl,'w') as fl:
		for ln in finallinks:
			fl.write(ln+"\n")

	with open("downloaded.txt",'a') as fl:
		for ln in finallinks:
			fl.write(ln+"\n")


def main():

	dir = sys.argv[1]

	os.chdir(dir)

	newfl = dir+".txt"
	oldfl = "old"+dir+".txt"

	findUnique(newfl,oldfl)

if __name__ == "__main__":
	main()
