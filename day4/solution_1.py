#bruh idek im going to use brute force

data = open("day4/input.txt", "r")
data = data.readlines()
data = [list(i) for i in data]
count = 0
for line in data:
    new_line = line[::-1]
    for index in range(0,len(line)):
        if line[index:index+4] == list('XMAS'):
            count+=1
        if new_line[index:index+4] == list('XMAS'):
            count+=1
transposed = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
for line in transposed:
    new_line = line[::-1]
    for index in range(0,len(line)):
        if line[index:index+4] == list('XMAS'):
            count+=1
        if new_line[index:index+4] == list('XMAS'):
            count+=1
for d in range(-len(data) + 1, len(data[0])): 
    diagonal = [data[i][i - d] for i in range(max(0, d), min(len(data), len(data[0]) + d))]
    new_line = diagonal[::-1]
    for index in range(0,len(diagonal)):
        if diagonal[index:index+4] == list('XMAS'):
            count+=1
        if new_line[index:index+4] == list('XMAS'):
            count+=1
for d in range(len(data) + len(data[0]) - 1):  # Covers all secondary diagonals
    diagonal = [data[i][d - i] for i in range(max(0, d - len(data[0]) + 1), min(len(data), d + 1))]
    new_line = diagonal[::-1]
    for index in range(0,len(diagonal)):
        if diagonal[index:index+4] == list('XMAS'):
            count+=1
        if new_line[index:index+4] == list('XMAS'):
            count+=1

print(count)
    
    


