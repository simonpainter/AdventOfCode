inputrange = range(145852,616942)
output = []

for input in inputrange:
    input = list(map(int, str(input)))

    sorted_list = input[:]
    sorted_list.sort()
    if (sorted_list == input) and (list(set(input)) != input):
        output.append(input)
        print (input)

print(len(output))
