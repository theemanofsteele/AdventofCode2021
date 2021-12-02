# Part 1
def getchangecount(inputlist):
    changecount = 0
    for i in range(len(inputlist)):
        if i == 0:
            continue
        if inputlist[i] > inputlist[i - 1]:
            changecount += 1
    return changecount


# Part 2
def buildrollinglist(inputlist):
    rolledlist = []
    for i in range(len(inputlist) - 2):
        rolledlist.append(inputlist[i] + inputlist[i + 1] + inputlist[i + 2])
    return rolledlist


# Main Execution
depths = open("input.txt", "r")
depthsArray = []

for depth in depths.readlines():
    depthsArray.append(int(depth.strip()))

print(getchangecount(depthsArray))
print(getchangecount(buildrollinglist(depthsArray)))
