import re
holding = {}
weights = {}
with open ("input.txt", "r") as inputfile:
	for line in inputfile:
		count = 0
		hold = set()
		for word in line.split():
			if(count == 0):
				name = str(word)
			elif(count == 1):
				weights[name] = int(word.strip('()'))
			else:
				if(len(word) is not 2):
					hold.add(word.strip(','))
			count += 1
			if(len(hold) > 0):
				holding[name] = hold



base = 'vmpywg'

def holding_weight(disc_holder):
	value = []
	value.append(weights[disc_holder])

	if disc_holder in holding:
		disc=[]
		for held in holding[disc_holder]:
			disc.append(holding_weight(held))
		value.extend(disc)
		if max(disc)!=min(disc):
			print(disc)
			print(disc_holder)
			for held in holding[disc_holder]:
				print(weights[held])
	return sum(value)


holding_weight(base)
