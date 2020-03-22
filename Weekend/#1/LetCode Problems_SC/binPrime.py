class Solution:
    def isPrime(self, number) :
        if number >= 2 :
            for i in range(2, number) :
                if number % i == 0 :
                    return False
                    break
            return True
        else :
            return False
        
    def countPrimeSetBits(self, L: int, R: int) -> int:
        res = 0
        for i in range(L, R+1) :
            str_i = bin(i)
            n = str_i.count('1')
            if self.isPrime(n) == True :
                res += 1
        return res