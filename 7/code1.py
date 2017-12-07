import re
with open ("input.txt", "r") as inputfile:
	data=inputfile.read()
names = re.findall('[a-z]+', data)
names=sorted(names)

for name in names:
    if (name != names[(names.index(name))+1]) and (name != names[names.index(name)-1]):
        print(name)
