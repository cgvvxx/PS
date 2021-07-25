# Baekjoon 14921 - 용액 합성하기
# Gold 5
# 투포인터

n = int(input())
arr = list(map(int, input().split()))

start_idx = 0
end_idx = len(arr)-1

mixed = arr[start_idx] + arr[end_idx]
best = mixed

while end_idx - start_idx > 1:
    
    if mixed == 0:
        print(0)
        break
    elif mixed < 0:
        start_idx += 1
        mixed += arr[start_idx] - arr[start_idx-1]
    else:
        end_idx -= 1
        mixed += arr[end_idx] - arr[end_idx+1]
        
    if abs(best) > abs(mixed):
            best = mixed
    
print(best)