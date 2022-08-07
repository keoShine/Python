def collatz(n):
    return int(n/2) if n % 2 == 0 else 3*n + 1

collatz_dict = {
    1: 0
}

temp = []
counter = 0

for i in range(2, 50):
    j = i
    while j not in collatz_dict.keys():
        temp.append(j)
        j = collatz(j)
        counter += 1
    for k in range(len(temp)):
        collatz_dict.update({temp[k]: collatz_dict.get(j) + counter - k})
    temp = []
    counter = 0

collatz_dict = dict(sorted(collatz_dict.items()))
for i in collatz_dict:
    print(str(i) + ": " + str(collatz_dict[i]))

