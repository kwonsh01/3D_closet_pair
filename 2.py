import sys
      
def BF(list, start, end):
    min_value = 4300000000
    temp = 0
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            temp = abs(list[i][0] - list[j][0]) + abs(list[i][1] - list[j][1]) + abs(list[i][2] - list[j][2])
            if(temp < min_value):
                min_value = temp
    return min_value

def bnd_y(list, delta):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if(delta < abs(list[i][1] - list[j][1])):
                break
            temp = abs(list[i][0] - list[j][0]) + abs(list[i][1] - list[j][1]) + abs(list[i][2] - list[j][2])
            if(temp < delta):
                delta = temp
    return delta

def bnd_z(list, delta):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if(delta < abs(list[i][2] - list[j][2])):
                break
            temp = abs(list[i][0] - list[j][0]) + abs(list[i][1] - list[j][1]) + abs(list[i][2] - list[j][2])
            if(temp < delta):
                delta = temp
    return delta

def closet_p_y(list_y, Sorted_z, start, end):
    if(end - start <= 2):
        return BF(list_y, start, end)
    else:
        m = (start + end) // 2
        midpoint = list_y[m]
        
        low_z = []
        high_z = []
        
        LH = 0
        
        for Y in range(len(Sorted_z)):
            if(Sorted_z[Y][1] < midpoint[1]):
                low_z.append(Sorted_z[Y])
            elif(Sorted_z[Y][1] > midpoint[1]):
                high_z.append(Sorted_z[Y])
            else:
                if(LH):
                    low_z.append(Sorted_z[Y])
                    LH = 0
                else:
                    high_z.append(Sorted_z[Y])
                    LH = 1
                           
        lowmin = closet_p_y(list_y, low_z, start, m)
        hightmin = closet_p_y(list_y, high_z, m, end)
        delta = lowmin if lowmin < hightmin else hightmin
        
        junc = []
        for i in range(0, len(Sorted_z)):
            if(abs(Sorted_z[i][1] - midpoint[1]) < delta):
                junc.append(Sorted_z[i])

        minimum = bnd_z(junc, delta)
        
        return min(delta, minimum)
    
def closet_p_x(list_x, list_y, start, end):
    if(end - start <= 2):
        return BF(list_x, start, end)
    else:
        m = (start + end) // 2
        midpoint = list_x[m]
        
        left_y = []
        right_y = []
        
        LR = 0
        
        for Y in range(len(list_y)):
            if(list_y[Y][0] < midpoint[0]):
                left_y.append(list_y[Y])
            elif(list_y[Y][0] > midpoint[0]):
                right_y.append(list_y[Y])
            else:
                if(LR):
                    left_y.append(list_y[Y])
                    LR = 0
                else:
                    right_y.append(list_y[Y])
                    LR = 1        
        
        leftmin = closet_p_x(list_x, left_y, start, m)
        rightmin = closet_p_x(list_x, right_y, m, end)
        delta = leftmin if leftmin < rightmin else rightmin
        
        junc = []
        for i in range(0, len(list_y)):
            if(abs(list_y[i][0] - midpoint[0]) < delta):
                junc.append(list_y[i])
                
        Sorted_z = sorted(junc, key=lambda x:x[2])
        
        minimum = closet_p_y(junc, Sorted_z, 0, len(junc) - 1)
        
        return min(delta, minimum)   

testcase = int(input())

for i in range(testcase):
    num = int(input())
    point = []
    for j in range(num):
        point.append(list(map(int, sys.stdin.readline().split())))
        
    point.sort(key=lambda x:x[0])
    sorted_y = sorted(point, key=lambda x:x[1])
    min_vv = closet_p_x(point, sorted_y, 0, len(point) - 1)
    print(min_vv)