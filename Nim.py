turn = 0
winstate = False
players = 2 #int(input("Number of players: "))
max_removes = 0 #If max_removes == 0, there is no limit on the number of counts that can be removed per turn

#Make piles
def make_piles():
    p = []
    i = 0
    while True:
        counters = input("Counters in pile " + str(i) + ": " )
        q = int(counters) if counters != '' else 0
        if q > 0:
            p.append(q)
            i += 1
        elif q == 0 and i == 0:
            print("At least one pile must be made..")
        elif q < 0:
            print("A pile cannot have negative counters")
        else:
            return p

#Return index of current player's turn with input of total number of players
def player_turn(x):
    global turn
    return turn % x

#Incriment the turn counter
def turn_inc():
    global turn
    turn += 1
    return

piles = make_piles()

#Check whether all piles have been reduced to 0
def check_win():
    global winstate
    global piles
    for i in piles:
        if i != 0:
            return
        else:
            winstate = True

#remove x counters from pile y
def remove_counters(x, y = 0):
    global max_removes
    global turn
    global winstate
    global players
    global piles
    if y >= len(piles):
        print("Invalid pile; there are " + str(len(piles)) + " piles in play..")
        return
    if x > max_removes and max_removes != 0:
        print("Invalid move; a maximum of " + str(max_removes) + " can be removed per turn..")
    elif x == 0:
        print("Invalid move; at least one counter must be removed per turn..")
    elif piles[y] == 0:
        print("Invalid move; pile " + str(y) + " has no counters left to remove..")
    elif x > piles[y]:
        print("Taking remaining " + str(piles[y]) + " counters from pile " + str(y) + "..")
    else:
        piles[y] -= x
        print("Removing " + str(x) + " counters from pile " + str(y) + ".. " + str(piles[y]) + " counters are left in pile " + str(y) + "..")
        print("")
        check_win()
        if winstate == True:
            print("Player " + str(player_turn(players) + 1) + " wins..")
        else:
            turn_inc()
            print("")
            print("Remaining piles: " + str(piles))

#Bitwise xor across all piles
def nim_sum(n):
    global max_removes
    sum = 0
    for i in n:
        sum = sum ^ i if max_removes == 0 else sum ^ (i % (max_removes + 1))
    return sum

def optimal_move(n):
    res = [0, 0]
    p = nim_sum(n)
    if p == 0:
        print("No optimal move; opponent will win with optimal play")
        for i in range(len(n)):
            if n[i] != 0:
                res = [1, i]
            break
    else:
        k = len(bin(p)) - 3
        for i in range(len(n)):
            if (n[i] >> k) % 2 == 1:
                if n[i] - (n[i] ^ p) > res[0]: res = [n[i] - (n[i] ^ p), i]
    return res


while winstate == False:
    x = int(input("Counters to remove: "))
    y = int(input("Pile to remove counters from: ")) if len(piles) > 1 else 0
    remove_counters(x, y)

input("Press any key to exit..")