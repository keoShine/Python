collatz = lambda n : 3 * n + 1 if n % 2 else int(n/2)

collatz_dict = {1: 0}

bound = 1000

for i in range(2, bound):
    temp = []
    j = i
    while j not in collatz_dict:
        temp.append(j)
        j = collatz(j)
    tdict = dict(zip(temp, list(range(len(temp) + collatz_dict[j], collatz_dict[j] - 1, -1))))
    collatz_dict.update(tdict)

for i in range(1, bound + 1):
    print("{:d}: {:d}".format(i, collatz_dict[i]))

