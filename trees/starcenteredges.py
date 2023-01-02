#1791. Find Center of Star Graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashAdj={}
        n=len(edges)
        for i in edges:
            if i[0] in hashAdj.keys():
                hashAdj[i[0]]+=1
                if hashAdj[i[0]] == n:
                    return i[0]
            else:
                hashAdj[i[0]]=1
            if i[1] in hashAdj.keys():
                hashAdj[i[1]]+=1
                if hashAdj[i[1]] == n:
                    return i[1]
            else:
                hashAdj[i[1]]=1
            