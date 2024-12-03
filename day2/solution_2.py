
def idek(x, chance):
    index = 0
    iod = 'i' if x[0] < x[1] else 'd'
    while index < len(x)-1:
        y = x[index+1] - x[index] if iod == 'i' else  x[index] - x[index+1]
        if y < 1 or y >3:
                if chance:
                    return idek(x[:index+1] + x[index+2:], 0) or idek(x[:-1], 0) or idek(x[1::], 0) or idek(x[:index] + x[index+1:], 0)
                else:
                     return 0
        index+=1
    return 1

data = open("day2/input.txt", "r")
real_data = data.readlines()
count = 0
for i in real_data:
    x = list(map(int, i.split()))
    count +=idek(x,1)
print(count)



