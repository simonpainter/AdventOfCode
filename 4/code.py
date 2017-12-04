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
total1=0
total2=0
for passphrase in list:
	if sorted(set(passphrase)) == sorted(passphrase):
		total1+=1
	list = []
	for password in passphrase:
		list.append(''.join(sorted(password)))
	if sorted(set(list)) == sorted(list):
		total2+=1

print(total1)
print(total2)
