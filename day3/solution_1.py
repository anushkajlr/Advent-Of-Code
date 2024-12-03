import re
data = open("/Users/anushkajalori/Desktop/aoc/day/day3/input.txt").read().replace("\n", "")
res = 0
pattern = r"^mul\((\d{1,3}),(\d{1,3})\)"
index = 0
while index < len(data):
    match = re.match(pattern, data[index:])
    if match:
            res += int(match.group(1)) * int(match.group(2))
    index += 1
    
print(res)

