class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = {'U' : [0,1], 'D': [0,-1], 'L' : [1,0], 'R': [-1,0]}
        res = []
        for i in moves :
            res.append(x[i])
        x = 0
        y = 0
        for j in res :
            x += j[1]
            y += j[0]
        if [x, y] == [0, 0] :
            return True
        else :
            return False
        