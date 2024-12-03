#part 2

data = open("/Users/anushkajalori/Desktop/aoc/day/day1/input.txt", "r")
real_data = data.readlines()
l1=[]
l2={}
for i in real_data:
    l1.append(int(i.split()[0]))
    x = int(i.split()[1])
    if x in l2:
        l2[x] += 1
    else:
        l2[x] = 1
count = 0
for i in l1:
    count += i * l2[i] if i in l2 else 0

print(count)