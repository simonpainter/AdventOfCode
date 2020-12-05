passes = []

def read_boarding(input):
	rowdata = input[0:7]
	coldata = input[7:]
	rowdata = rowdata.replace('F','0')
	rowdata = rowdata.replace('B','1')
	rowdec = int(rowdata, 2)

	coldata = coldata.replace('L','0')
	coldata = coldata.replace('R','1')
	coldec = int(coldata, 2)

	return rowdec * 8 + coldec

with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
	for line in data:
		passes.append(read_boarding(line))

for seat in range(0,(128*8)):
	if (seat not in passes) and (seat-1 in passes) and (seat+1 in passes):
		print(seat) 

