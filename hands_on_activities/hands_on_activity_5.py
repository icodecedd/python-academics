players = []
eliminated = []
def inputPlayers():
    print("Inputs: ")
    size = int(input("Number of Player (8-20): "))
    while size > 20 or size  < 8:
        size = int(input("Number of Player (8-20): "))

    for i in range(1, size+1):
        players.append(i)

    start = int(input("Starting Point/Player Position: "))
    while start > size or start < 1:
        start = int(input("Starting Point/Player Position: "))

    skips = int(input("Number of Skips: "))
    while skips > size or skips < 1:
        skips = int(input("Number of Skips: "))

    direct = input("Direction: ")
    while direct != "clockwise" and direct != "counter clockwise":
        direct = input("Direction: ")

    return size, start, skips, direct

def killPlayer(numStarts, numSkips):
    length = len(players)-1
    startPoint = players.index(numStarts)
    while length > 0:
        startPoint += numSkips-1 # subtract 1 in number of skips as the length decreases
        while startPoint > length:
            startPoint -= length+1
        eliminated.append(players[startPoint])
        length -= 1
        players.pop(startPoint)
    if dDirect == "counter clockwise":
        for i in range(sSize):
            j=-1
            j-=i

if __name__ == '__main__':
    sSize, sStarts, sSkips, dDirect = inputPlayers()
    killPlayer(sStarts, sSkips)
    print("Outputs: ")
    print("Position of players killed:")
    finalEliminated = ", ".join(map(str, eliminated))
    print(finalEliminated)
    print(f"Last Player: {players[0]}")
