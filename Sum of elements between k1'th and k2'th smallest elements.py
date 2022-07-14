class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        A.sort()
        c=K1-1
        d=K2
        e=A[(c+1):(d-1)]
        sum =0
        for i in e:
            sum=sum+i
        return sum
