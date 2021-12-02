# Main Execution
locations = open("input.txt", "r")
locationstuple = []
horizontalpostion = 0
verticalposition = 0

for location in locations.readlines():
    locationstuple.append((location.strip()).split(" "))

for item in locationstuple:
    if item[0] == "forward":
        horizontalpostion += int(item[1])
    elif item[0] == "down":
        verticalposition += int(item[1])
    elif item[0] == "up":
        verticalposition -= int(item[1])

print("Vertical Position: " + str(verticalposition))
print("Horizontal Position: " + str(horizontalpostion))
print("Position: " + str(horizontalpostion * verticalposition))