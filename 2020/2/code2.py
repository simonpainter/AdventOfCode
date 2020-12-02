result = 0
with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

for line in data:
	password = line.strip().split(":")[1]
	character = line.strip().split(":")[0].split()[1]
	upper = int(line.strip().split(":")[0].split()[0].split("-")[1])
	lower = int(line.strip().split(":")[0].split()[0].split("-")[0])
	if (password[lower]==character)^(password[upper]==character):
		result +=1

print(result)
