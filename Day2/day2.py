# Main Execution
locations = open("input.txt", "r")
locationstuple = []
horizontalpostion = 0
depth = 0

for location in locations.readlines():
    locationstuple.append((location.strip()).split(" "))

# Part 1 -----------------------------------------
for item in locationstuple:
    if item[0] == "forward":
        horizontalpostion += int(item[1])
    elif item[0] == "down":
        depth += int(item[1])
    elif item[0] == "up":
        depth -= int(item[1])

print("*** Part 1 ***")
print("Vertical Position: " + str(depth))
print("Horizontal Position: " + str(horizontalpostion))
print("Position: " + str(horizontalpostion * depth))
# -------------------------------------------------------
# Part 2 ------------------------------------------------
horizontalpostion = 0
depth = 0
aim = 0
for item in locationstuple:
    if item[0] == "forward":
        horizontalpostion += int(item[1])
        depth += int(item[1]) * aim
    elif item[0] == "down":
        aim += int(item[1])
    elif item[0] == "up":
        aim -= int(item[1])

print("\n*** Part 2 ***")
print("Vertical Position: " + str(depth))
print("Horizontal Position: " + str(horizontalpostion))
print("Position: " + str(horizontalpostion * depth))
# -------------------------------------------------------
