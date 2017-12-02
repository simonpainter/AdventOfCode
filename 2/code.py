spreadsheet = []
checksum1 = []
checksum2 = []

with open ("input.txt", "r") as inputfile:
        data=inputfile.readlines()
for line in data:
	linedata = line.split("\t")
	row = []
	for cell in linedata:
		row.append(int(cell.strip()))
	spreadsheet.append(row)
	checksum1.append(max(row) - min(row))
	for cell in row:
		for i in range(0, len(row)):
			if ((cell % row[i]) == 0):
				if (cell/row[i]) > 1:
					checksum2.append(cell/row[i])

print(sum(checksum1))
print(sum(checksum2))

