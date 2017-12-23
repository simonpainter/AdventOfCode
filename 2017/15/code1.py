a = 512
b = 191
bits = 65535
count = 0


def increment(input,gen):
    output = 1
    if gen == "a":
        while output % 4 !=0:
            input = input * 16807
            output = input % 2147483647
    else:
        while output % 8 !=0:
            input = input * 48271
            output = input % 2147483647

    return output

for i in range(1,5000000):
    a = increment(a,"a")
    b = increment(b,"b")

    if (a & bits) == (b & bits):
        count +=1

print(count)
