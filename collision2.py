import hashlib
import os

doglist = []
catlist = []
fdog = open("dog.jpg", 'r')
fcat = open("cat.jpg", 'r')
dogContent = fdog.read()
catContent = fcat.read()
fdog.close()
fcat.close()
md5Dog = hashlib.md5(dogContent)
md5Cat = hashlib.md5(catContent)
done = False
md5DogCopy = md5Dog.copy()
md5CatCopy = md5Cat.copy()


for i in range(0, 10000000):
	md5DogCopy.update(str(0))
	dogHash = md5DogCopy.hexdigest()[:10]
	doglist.append(dogHash)

for i in range(0, 10000000):
	md5CatCopy.update(str(0))
	catHash = md5CatCopy.hexdigest()[:10]
	catlist.append(catHash)

counter = 0
while not done:
	md5DogCopy.update(str(0))
	dogHash = md5DogCopy.hexdigest()[:10]
	doglist.append(dogHash)
	md5CatCopy.update(str(0))
	catHash = md5CatCopy.hexdigest()[:10]
	catlist.append(catHash)
	counter += 1
	print counter
	if len(set(doglist).intersection(catlist)) > 0:
		print "Found Collision"
		inter = set(doglist).intersection(catlist)
		print "Dog Zeroes: %d, Cat Zeros: %d" %(doglist.index(list(inter)[0]), catlist.index(list(inter)[0]))
		done = True