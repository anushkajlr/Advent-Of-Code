data =  open("day5/input.txt", "r").readlines()
#2|3
# 2,3
#3,2
# {2:3}

rules = {}
count = 0
start_test = False
for line in data:
    test = 0
    if start_test:
        line = line.strip("\n").split(",")
        for i in range(len(line)-1):
            for j in range(i+1, len(line)):
                if line[j] in rules and line[i] in rules[line[j]]:
                    test = 1
                    temp = line[j]
                    line[j] = line[i]
                    line[i] = temp
        if test:
            count += int(line[int((len(line)-1)/2)])
    else:
        if line.strip("\n").split("|") == ['']:
            start_test = True
            # start testing logic
            
        else:
        
            a,b = line.strip("\n").split("|")
            if a in rules:
                rules[a].append(b)
            else:
                rules[a] = [b]
print(count)

