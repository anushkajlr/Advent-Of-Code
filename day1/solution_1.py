
data = open("day1/input.txt", "r")
real_data = data.readlines()
l1=[]
l2=[]
for i in real_data:
    l1.append(int(i.split()[0]))
    l2.append(int(i.split()[1]))
l1.sort()
l2 .sort() 
count = 0
for i in range(len(l1)):
    count += l1[i] - l2[i] if l1[i] - l2[i] > 0 else (l1[i] - l2[i]) *-1

print(count)





