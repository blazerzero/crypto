import io
import hashlib
import random
import base64
import string
import sys

def stringgen(size = 10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def intersect(cats, dogs):
    return list(set(cats) & set(dogs))

def main():
    print("Hello")
    cathasher = hashlib.md5()
    doghasher = hashlib.md5()

    chash10 = []
    dhash10 = []

    with open("cat.jpg", "rb") as catfile:
        catbuf = base64.b64encode(catfile.read())

    with open("dog.jpg", "rb") as dogfile:
        dogbuf = base64.b64encode(dogfile.read())

    catfile.close()
    dogfile.close()

    catbuf_new = catbuf
    dogbuf_new = dogbuf

    catfile = open("cat.jpg", "a")
    dogfile = open("dog.jpg", "a")

    cathasher.update(catbuf)
    doghasher.update(dogbuf)

    print(catbuf)
    print(dogbuf)

    cathash = cathasher.hexdigest()
    doghash = doghasher.hexdigest()

    chash10.append(cathash[0:9])
    dhash10.append(doghash[0:9])

    catgenfull = ""
    doggenfull = ""
    print(intersect(chash10, dhash10))

    for i in range(0,9999999):
        catgen = stringgen()
        doggen = stringgen()


        cathasher.update(catgen)
        doghasher.update(doggen)

        cathash = cathasher.hexdigest()
        doghash = doghasher.hexdigest()
        print(cathash[0:9])
        print(doghash[0:9])
        #cats_full.append(cathash)
        #dogs_full.append(doghash)
        chash10.append(cathash[0:9])
        dhash10.append(doghash[0:9])

    while (intersect(chash10, dhash10) == []):
        catgen = stringgen()
        doggen = stringgen()

        cathasher.update(catgen)
        doghasher.update(doggen)

        cathash = cathasher.hexdigest()
        doghash = doghasher.hexdigest()
        print(cathash[0:9])
        print(doghash[0:9])
        chash10.append(cathash[0:9])
        dhash10.append(doghash[0:9])

    catfile.write(catgen)
    catfile.write(doggen)
    catfile.close()
    dogfile.close()

main()
