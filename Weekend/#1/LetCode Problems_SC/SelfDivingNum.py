class Solution:
    def selfDividingNumbers(self, left: int, right: int) : #-> List[int]:
        res = []

        for y in range(left, right+1) :
            num = y
            list_number = []
            while num > 0 :
                satuan = num % 10
                list_number.append(satuan)
                num = num//10
            if 0 in list_number :
                continue
            else :
                count = 0
                for i in list_number :
                    if y % i != 0 :
                        count += 1
                if count == 0 :
                    res.append(y)
        return res