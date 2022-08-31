# solved: [2287] 모노디지털 표현
# https://www.acmicpc.net/problem/2287
# dp
# 
# Gold 2
# k표현의 길이가 1~8인 모든 경우를 monos라는 dictionary에 저장 후 해당하는 k의 길이를 return
# k표현의 길이가 1인 경우 {k}
# k표현의 길이가 2인 경우 {2k=k+k, 1=k/k, k**2=k*k, 11*k='kk'}
# k표현의 길이가 3이상인 경우, 그 보다 작은 k표현의 길이의 합으로 구할 수 있는 모든 케이스를 체크
# ex. k표현의 길이가 4인 경우, k표현의 길이 1과 k표현의 길이 3인 경우의 조합 + k표현의 길이 2인 2개의 조합 + 'kkkk'
# 추가로 k표현의 길이보다 작을 때 나오는 수는 해당 k표현의 길이에 저장 X

def monodigit(k):
    
    monos = dict()
    
    monos[1] = set([k])
    monos[2] = set([1, 2*k, k**2, 11*k])
    notin = monos[1] | monos[2]
    
    for m in range(3, 9):
        monos[m] = set()
        monos[m].add(int('1'*m)*k)
        for i in range(1, m//2+1):
            
            for a in monos[i]:
                for b in monos[m-i]:
                    checks = [a+b, a*b, a-b, b-a]
                        
                    if b != 0:
                        checks.append(a//b)
                    
                    if a != 0:
                        checks.append(b//a)
                    
                    for check in checks:
                        if check > 0 and check not in notin:
                            monos[m].add(check)
                            
        notin |= monos[m]
                            
    return monos

def get_least_mono(n):
    
    for i in range(1, 9):
        if n in monos[i]:
            print(i)
            return
        
    print("NO")
    return


k = int(input())
nums = [int(input()) for _ in range(int(input()))]
monos = monodigit(k)
for n in nums:
    get_least_mono(n)
