import hashlib

input = "ckczppom"
x = 0
hash = ""

while hash[:6] != "000000":
    hash = hashlib.md5(input+str(x)).hexdigest()
    print x,hash
    x+=1
