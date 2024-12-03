import re
data = open("/Users/anushkajalori/Desktop/aoc/day/day3/input.txt").read().replace("\n", "")

res = 0


pattern = r"^mul\((\d{1,3}),(\d{1,3})\).*"
dopat = r"^do\(\).*"
dontpat = r"^don\'t\(\).*"

res = 0
index = 0
pop = 0
while index < len(data):
    match = re.match(pattern, data[index:])
    domatch = re.match(dopat, data[index:] )
    dontmatch = re.match(dontpat, data[index:])
    if match and not pop:
            res += int(match.group(1)) * int(match.group(2))
    if dontmatch:
        pop = 1
    if domatch:
        pop = 0
    index += 1
    
print(res)

