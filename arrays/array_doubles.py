# 954. Array of Doubled Pairs

# Day 3 : hashmap embarassment
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        # print(arr)
        newMap={}
        for i in arr:
            if i not in newMap:
                newMap[i]=1
                continue
            newMap[i] +=1
        # print(newMap)
        for i in arr:
            if i < 0: 
                # [-8,-4,-4,-2]
                # check its still valid 
                if i in newMap:
                    if i/2 in newMap:
                        newMap[i/2]-=1
                        if newMap[i/2] == 0:
                            newMap.pop(i/2)
                    else:
                        return False
                    newMap[i]-=1
                    if newMap[i] == 0:
                        newMap.pop(i)
                else:
                    continue
            elif i > 0:
                # [2,4,4,8]
                if i in newMap:
                    if i*2 in newMap:
                        newMap[i*2]-=1
                        if newMap[i*2] == 0:
                            newMap.pop(i*2)
                    else:
                        return False
                    newMap[i]-=1
                    if newMap[i] == 0:
                        newMap.pop(i)
                else:
                    continue
                    
                # check its half presense  
            else:
                if newMap[i]%2 == 0:
                    continue
                else:
                    return False 

        return True