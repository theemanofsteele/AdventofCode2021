import re
import numpy
from pprint import pprint

vents = open("inputs.txt", "r")
lines = []
for vent in vents:
    lines.append(re.findall(r'\d+', vent))

lines = numpy.array(lines).astype(int)

grid_max = numpy.max(lines)
grid_array = []
for x in range(grid_max + 1):
    row = []
    for y in range(grid_max + 1):
        row.append('.')
    grid_array.append(row)


def mark_vertical_line(equal, a, b, grid):
    if abs(a - b) > 0:
        if a > b:
            start = b
            end = a
        else:
            start = a
            end = b

        while start <= end:
            if grid[start][equal] == '.':
                grid[start][equal] = '1'
            else:
                grid[start][equal] = str(int(grid[start][equal]) + 1)
            start += 1


def mark_horizontal_line(equal, a, b, grid):
    if abs(a - b) > 0:
        if a > b:
            start = b
            end = a
        else:
            start = a
            end = b

        while start <= end:
            if grid[equal][start] == '.':
                grid[equal][start] = '1'
            else:
                grid[equal][start] = str(int(grid[equal][start]) + 1)
            start += 1


for x1, y1, x2, y2 in lines:
    if x1 == x2:
        mark_vertical_line(x1, y1, y2, grid_array)
    if y1 == y2:
        mark_horizontal_line(y1, x1, x2, grid_array)


print("Over lapping points: " + str(numpy.count_nonzero(numpy.array(grid_array) >= '2')))
