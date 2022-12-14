
def minArea(cord):
    #unique = set(cord) # set = cord
    #haspMap((1,1))
    minArea = 9999999
    for x in cord: #[1,1]
        for y in cord:
            k = y[0]-x[0] # 1
            z = y[1] - x[1] # 1
            if k == 0 or z ==0:
                continue
            if [i[0],i[1]+z] in cord and [i[0]+k,i[1]] in cord:
                # rectangle
                area=z*k
                if minArea > area:
                    minArea = area
    if minArea == 9999999:
        return -1
    print(minArea)
    return minArea
    