import io
import hashlib
import random
import base64
import string
import sys

def stringgen(size = 10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def intersect(cats, dogs):
    return list(set(cats) & set(dogs))

def main():
    print("Hello")
    cathasher = hashlib.md5()
    doghasher = hashlib.md5()
    cats_full = []
    dogs_full = []
    chash10 = []
    dhash10 = []

    with open("cat.jpg", "rb") as catfile:
        catbuf = base64.b64encode(catfile.read())

    with open("dog.jpg", "rb") as dogfile:
        dogbuf = base64.b64encode(dogfile.read())

    catfile.close()
    dogfile.close()

    catfile = open("cat.jpg", "a")
    dogfile = open("dog.jpg", "a")

    cathasher.update(catbuf)
    doghasher.update(dogbuf)

    print(catbuf)
    print(dogbuf)

    cathash = cathasher.hexdigest()
    doghash = doghasher.hexdigest()

    cats_full.append(cathash)
    dogs_full.append(doghash)
    chash10.append(cathash[0:9])
    dhash10.append(doghash[0:9])

    catgenfull = ""
    doggenfull = ""
    print(intersect(chash10, dhash10))
    for i in range(0,9999999):
        catgen = stringgen()
        doggen = stringgen()

        catgenfull+=catgen
        doggenfull+=catgen

        catbuf+=catgen
        dogbuf+=doggen

        cathasher.update(catbuf)
        doghasher.update(dogbuf)

        cathash = cathasher.hexdigest()
        doghash = doghasher.hexdigest()
        cats_full.append(cathash)
        dogs_full.append(doghash)
        chash10.append(cathash[0:9])
        dhash10.append(doghash[0:9])

    while (intersect(chash10, dhash10) == []):
        catgen = stringgen()
        doggen = stringgen()

        catgenfull+=catgen
        doggenfull+=catgen

        catbuf+=catgen
        dogbuf+=doggen

        cathasher.update(catbuf)
        doghasher.update(dogbuf)

        cathash = cathasher.hexdigest()
        doghash = doghasher.hexdigest()
        cats_full.append(cathash)
        dogs_full.append(doghash)
        chash10.append(cathash[0:9])
        dhash10.append(doghash[0:9])
        
    catfile.write(catgenfull)
    catfile.write(doggenfull)
    catfile.close()
    dogfile.close()

main()
