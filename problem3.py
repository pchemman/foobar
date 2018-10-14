def answer(src, dest):
    if dest == src:
        return 0
    def validmoves(start):
        moves = [(-2,-1), (-2,1), (-1,2), (-1,-2), (1,2), (1,-2), (2,-1), (2,1) ]
        col = start % 8
        row = int(start / 8)
        endpt = []
        for move in moves:
            newc = col + move[0]
            newr = row + move[1]
            if not (newc < 0 or newr < 0 or newc > 7 or newr > 7):
                endpt.append(newr*8+newc)
        return endpt

    set = [[] for i in range(7)]
    set[0].append(src)
    for i in range(0, 6):
        for item in set[i]:
            listmoves = validmoves(item)
            if dest in listmoves:
                return i+1
            else:
                for next in listmoves:
                    if not any(next in sublist for sublist in set):
                        set[i+1].append(next)
    return -99

print(answer(0, 1))
print(answer(19, 36))
print(answer(63, 0))
print(answer(0, 9))
print(answer(1,0))

print(answer(1,1))
# for i in range(0, 64):
#     for j in range(0, 64):
#         print(answer(i, j))
