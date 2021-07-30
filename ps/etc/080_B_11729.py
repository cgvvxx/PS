# Baekjoon 11729 - 하노이 탑 이동 순서
# Silver 2

def hanoi(n, _from, _to):
    
    if n == 1:
        route.append(f'{_from} {_to}')
        count.append(1)
        return
    
    _another = list(set([1, 2, 3]) - set([_from, _to]))[0]
    
    hanoi(n-1, _from, _another)
    hanoi(1, _from, _to)
    hanoi(n-1, _another, _to)
    
count = []
route = []
    
hanoi(int(input()), 1, 3)
print(sum(count))
for r in route:
    print(r)