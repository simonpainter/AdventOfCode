import re, itertools, math, hashlib

input = 'cxdnnyjw'
#input = 'abc'

def part1(input):
	index = 0
	count = 0
	password = list('########')
	print(''.join(password), end='\r')
	while '#' in password:
		str_candidate = input + str(index)
		candidate = str(hashlib.md5(str_candidate.encode()).hexdigest())
		if candidate[:5] == '00000':
			password[count]= candidate[5:6]
			print(''.join(password), end='\r')
			count +=1
		index+=1

	return ''.join(password)	

def part2(input):
	index = 0
	password = list('########')
	print(''.join(password), end='\r')
	while '#' in password:
		str_candidate = input + str(index)
		candidate = str(hashlib.md5(str_candidate.encode()).hexdigest())
		if candidate[:5] == '00000':
			position = str(candidate[5:6])
			if position in '01234567' and password[int(position)]=='#':
				password[int(position)]= candidate[6:7]
				print(''.join(password), end='\r')
		index+=1
	return ''.join(password)

#print(part1(input))
print(part2(input))