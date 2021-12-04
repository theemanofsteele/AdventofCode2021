import pandas as pd


def most_common(lst):
    return max(set(lst), key=lst.count)


def least_common(lst):
    return min(set(lst), key=lst.count)


def binarytodecimal(n):
    return int(n, 2)


binarynumbers = open("inputs.txt", "r")
binarymatrix = []
for item in binarynumbers.readlines():
    temparray = []
    for bit in item.strip():
        temparray.append(int(bit))
    binarymatrix.append(temparray)

dataframe = pd.DataFrame(binarymatrix)

# Part 1 -------------------------------------
gammastring = ""
for i in range(len(dataframe.columns)):
    gammastring += str(most_common(dataframe[i].tolist()))

epsilonstring = ""
for i in range(len(dataframe.columns)):
    epsilonstring += str(least_common(dataframe[i].tolist()))

print("*** Part 1 ***")
print("Power Consumption: " + str(binarytodecimal(gammastring) * binarytodecimal(epsilonstring)))


# ---------------------------------------------
# Part 2 --------------------------------------

def more_common(data):
    zeros = data.tolist().count(0)
    ones = data.tolist().count(1)
    if ones >= zeros:
        common = 1
    else:
        common = 0
    return common


def less_common(data):
    zeros = data.tolist().count(0)
    ones = data.tolist().count(1)
    if ones < zeros:
        common = 1
    else:
        common = 0
    return common


def getrating(data, rating):
    common = 0
    for i in range(len(data.columns)):
        if rating == "o2":
            common = more_common(data[i])
        elif rating == "co2":
            common = less_common(data[i])

        for row in data.iterrows():
            if len(dataframe.index) == 2:
                if row[1][i] == 0:
                    data = data.drop(row[0])
                    break

            if row[1][i] != common:
                data = data.drop(row[0])
        if len(data.index) == 1:
            break

    bitstring = ""
    for bit in data.iloc[0].to_string(header=False, index=False):
        bitstring += str(bit).strip()
    return binarytodecimal(bitstring)


oxygen = getrating(dataframe, "o2")
c02 = getrating(dataframe, "co2")
print("\n*** Part 2 ***")
print("Oxygen Generator Rating: " + str(oxygen))
print("C02 Scrubber Rating: " + str(c02))
print("Life Support Rating: " + str(oxygen * c02))
# ---------------------------------------------
