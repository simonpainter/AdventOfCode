triangles = []
success = []
with open ("input.txt", "r") as inputfile:
	lines=inputfile.readlines()
for line in lines:
	triangle = []
	for num in line.split():
		triangle.append(int(num))
	triangles.append(triangle)

for triangle in triangles:
	if max(triangle)<(sum(triangle)/2):
		success.append(1)

print(sum(success))
