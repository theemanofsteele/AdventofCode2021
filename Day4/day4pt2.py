import re
import numpy
from pprint import pprint


def check_winning_board(board):
    # Check across
    if 5 in numpy.count_nonzero(numpy.array(board) == 'x', axis=1):
        return True

    # Check vertically
    if 5 in numpy.count_nonzero(numpy.array(board) == 'x', axis=0):
        return True

    # Check Diagonally
    # if [board[i][i] for i in range(len(board[0]))].count('x') == 5:
    #     return True
    #
    # if [board[len(board[0]) - 1 - i][i] for i in range(len(board[0]) - 1, -1, -1)].count('x') == 5:
    #     return True

    return False


def get_sum_winning_card(board):
    sum = 0
    for row in board:
        for num in row:
            if re.findall(r'\d+', num):
                sum += int(num)
    return sum


bingo = open("inputs.txt", "r")
draws = []
for draw in bingo.readline().split(","):
    draws.append((draw.strip()))

counter = 0
bingocards = []
temparry = []
for line in bingo.readlines():
    temp = re.findall(r'\d+', line)
    if temp:
        # print(temp)
        temparry.append(temp)
        counter += 1
    if counter == 5:
        bingocards.append(temparry)
        temparry = []
        counter = 0

winner = False
lastcard = False
winnersum = 0
lastdraw = 0
for draw in draws:
    for x in reversed(range(len(bingocards))):
        for y in range(len(bingocards[x])):
            for z in range(len(bingocards[x][y])):
                if bingocards[x][y][z] == draw:
                    bingocards[x][y][z] = 'x'
                    winner = check_winning_board(bingocards[x])
                    if winner:
                        if len(bingocards) == 1:
                            winnersum = get_sum_winning_card(bingocards[x])
                            lastdraw = draw
                            lastcard = True
                            break
                        del bingocards[x]
                        break
            if winner:
                x += 1
                winner = False
                break
        if lastcard:
            break
    if lastcard:
        break

print("Winner Sum:" + str(winnersum))
print("Final Draw:" + str(lastdraw))
print("Final Score: " + str(int(winnersum) * int(lastdraw)))