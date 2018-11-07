triangles = []
matrix = []
success = []
with open ("input.txt", "r") as inputfile:
	lines=inputfile.readlines()

for line in lines:
	triangle = []
	for num in line.split():
		triangle.append(int(num))
	matrix.append(triangle)

for i in range(0,len(matrix),3):
	triangle0 = []
	triangle1 = []
	triangle2 = []
	for step in range(0,3):
		triangle0.append(matrix[i+step][0])
		triangle1.append(matrix[i+step][1])
		triangle2.append(matrix[i+step][2])

	triangles.append(triangle0)
	triangles.append(triangle1)
	triangles.append(triangle2)


for triangle in triangles:
	if max(triangle)<(sum(triangle)/2):
		success.append(1)

print(sum(success))
