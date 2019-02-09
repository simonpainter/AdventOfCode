def remove_at(i, s):
    return s[:i] + s[i+2:]

with open ("input.txt", "r") as inputfile:
    data=inputfile.readlines()
results = []
input = data[0].strip()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    testcase = input
    testcase = testcase.replace(letter, '')
    testcase = testcase.replace(letter.upper(), '')

    lasttest = ""
    while lasttest != testcase:
        lasttest = testcase
        for i in range(0, len(testcase)-1):
            if (testcase[i].isupper() and testcase[i+1].islower()) or (testcase[i].islower() and testcase[i+1].isupper()):
                if testcase[i].lower() == testcase[i+1].lower():
                    testcase = remove_at(i,testcase)
                    break
    results.append({letter:len(testcase)})
    print letter, len(testcase)
