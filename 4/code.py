from itertools import *
list = []
total = []
with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
for line in data:
	linedata = line.split()
	passphrase = []
	for password in linedata:
		passphrase.append(password.strip())
	list.append(passphrase)
#print(list)
for passphrase in list:
	tot=1
	c = combinations(passphrase,2)
	for t in c:
#		if t[0]==t[1]:
#			tot=0
		anagrams=permutations(t[0],(len(t[0])))
		for anagram in anagrams:
			print("".join(anagram))
			if ("".join(anagram)==t[1]):
				tot=0
	total.append(tot)

answer = sum(total)
print(answer)
