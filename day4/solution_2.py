can_be = [["M",".","S"],[".", "A", "."],["M",".","S"]]
also = [["M",".","M"],[".", "A", "."],["S",".","S"]]
also_be = [["S",".","S"],[".", "A", "."],["M",".","M"]]
also_can = [["S",".","M"],[".", "A", "."],["S",".","M"]]

data = open("day4/input.txt", "r")
data = data.readlines()
data = [list(i) for i in data]
count = 0
for i in range (len(data)):
        for j in range(len(data[0])):
                new = []
                for idk in range(i,i+3):
                    try:
                        new.append(data[idk][j:j+3])
                    except:
                            pass
                if len(new) == 3 and len(new[0]) == 3:
                    new[0][1] = "."
                    new[1][0] = '.'
                    new[1][2] = '.'
                    new[2][1] = '.'
            
                if new == can_be or new == also_can or new == also or new == also_be:
                        count+=1
print(count)
# 0 0 
# 1 0 
# 2 0 
# 0 1
# 1 1 
# 2 1


        