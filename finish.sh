mkdir -p "saved/"$1
mkdir $1
mv $1/$1".txt" $1/"old"$1".txt"
mv $1".txt" $1
python3 newLinks.py $1
python3 downloadFromFile.py
cd $1
python3 ../similarGroup.py .
