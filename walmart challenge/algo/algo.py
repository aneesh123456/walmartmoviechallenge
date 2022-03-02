import numpy as np
from collections import OrderedDict
movie_theatre = np.zeros((10,20))
myDict = OrderedDict()

def findBestSeats(n):
    temp = 0
    temp2 = []
    for i in range(len(movie_theatre)):
        for j in range(len(movie_theatre[0])):
            if checkPublicSafety(j,j+n,i) == True and checkSeats(j,j+n,i,n) == True:
                temp = 1
                temp2.append(i)

                for k in range(j, j+n):
                    movie_theatre[i][k] = 1
                    temp2.append(k)
                    
            if temp == 1:
                break
        if temp == 1:
            break
    return temp2


def checkPublicSafety(start, end, row):
    for i in range(1,4):
        if start - i > 0:
            if movie_theatre[row][start-i] == 1:
                return False
        if end + i <= 20:
            if movie_theatre[row][start+i] == 1:
                return False
    return True

def checkSeats(start, end, row, n):
    if(end > 20):
        return False
    for i in range(n):
        if movie_theatre[row][start+i] == 1:
            return False
    return True
s = open("./input" , "r")
contents = s.read().splitlines()
ids = []
nums = []
temp = []
for i in range(len(contents)):
    temp = contents[i].split(" ")
    ids.append(temp[0])
    nums.append(int(temp[1]))

for i in range(len(ids)):
    myDict[ids[i]] = findBestSeats(nums[i])

f1=open('./output', 'w+')
for key, value in myDict.items():
        f1.write(key + " "),
        print(key),
        for i in range(1,len(value)):
            if(i < len(value)-1):
                f1.write(chr(value[0]+65)+str(value[i]+1)+ ","),
                print(chr(value[0]+65)+str(value[i]+1)+ ","),
            else:
                f1.write(chr(value[0]+65)+str(value[i]+1)),
                print(chr(value[0]+65)+str(value[i]+1)),
        f1.write("\n")
        print("")
f1.close()




    
