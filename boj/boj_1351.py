# solved: [1351] 무한 수열
# https://www.acmicpc.net/problem/1351
# dp, recursion 
# 
# Gold 5
# 재귀적으로 주어진 수열의 값을 찾고, 이전에 나온 수열의 값은 dp와 같이 저장하여 return
# 이 때, n <= 10**12 이므로 단순히 dp를 리스트가 아닌 집합으로 저장해야 메모리 초과가 발생하지 않음

def get_a(n):
    
    if n == 0:
        return 1
    else:
        
        i = int(n/p)
        j = int(n/q)
        
        if i not in a:
            a[i] = get_a(i)
        
        if j not in a:
            a[j] = get_a(j)
        
        return a[i] + a[j]


n, p, q = map(int, input().split())
a = dict()
a[0] = 1
print(get_a(n))
