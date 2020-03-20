
# from hacker rank Rotate Left
# a is
# def rotLeft(a, d):
#     la = len(a)
#     temp = 0
#     for i in range(d) :
#         temp = a[0]
#         for j in range(0, len(a)-1) :
#             a[0] = a[]

ls = [1, 3, 5]
loop = 5
c = 0

for i in range(loop) :
    c = ls[0]
    for j in range(len(ls)-1) :
        ls[j] = ls[j+1]
    ls[len(ls)-1] = c

print(ls)


        

        


# rotLeft([1,2,3,4,5], 4)

