# 1번을 해보세요!
def find_max( A ): 
    max = A[0]
    for i in range(len(A)):
        if A[i] >max:
            max = A[i]
    return max

# 2번을 해보세요!
A = input()    # 20 34 12 93 84 39 64 55 24
A = A.split(' ')   # ['20', '34', '12', '93', '84', '39', '64', '55', '24']


array = list() # array = []

for n in A:
    array.append(int(n))


print(array, "최댓값=", find_max(array))