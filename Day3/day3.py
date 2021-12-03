import pandas as pd


def most_common(lst):
    return max(set(lst), key=lst.count)


def least_common(lst):
    return min(set(lst), key=lst.count)


def binaryToDecimal(n):
    return int(n,2)


binarynumbers = open("inputs.txt", "r")
binarymatrix = []
for item in binarynumbers.readlines():
    temparray = []
    for bit in item.strip():
        temparray.append(int(bit))
    binarymatrix.append(temparray)

dataframe = pd.DataFrame(binarymatrix)

gammastring = ""
for i in range(len(dataframe.columns)):
    gammastring += str(most_common(dataframe[i].tolist()))

epsilonstring = ""
for i in range(len(dataframe.columns)):
    epsilonstring += str(least_common(dataframe[i].tolist()))

print("*** Part 1 ***")
print("Power Consumption: " + str(binaryToDecimal(gammastring) * binaryToDecimal(epsilonstring)))

