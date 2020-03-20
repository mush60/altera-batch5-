class Solution:
    def fizzBuzz(self, n: int) : #-> List[str]:    
        flist = []
        for i in range(1,n+1) :
            if i % 3 == 0 :
                if i % 5 == 0 :
                    flist.append("FizzBuzz")
                else :
                    flist.append("Fizz")
            elif i % 5 == 0 :
                flist.append("Buzz")
            else :
                flist.append(str(i))
        return flist