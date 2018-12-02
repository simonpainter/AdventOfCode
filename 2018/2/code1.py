import re

with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
counttwo=0
countthree=0


for line in data:
    string =  "".join(sorted(line.strip()))
    p  = re.compile(r"((.)\2{1,})")
    if p.search(string):
        two = 0
        three = 0
        matches = p.findall(string)
        for match in matches:
            if len(match[0])==2:
                two = 1
            if len(match[0])==3:
                three = 1

        counttwo += two
        countthree += three

print counttwo,countthree, counttwo*countthree
