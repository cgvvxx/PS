# solved: [1026] 보물
# https://www.acmicpc.net/problem/1026
# greedy, sorting
# 
# Silver 4
# 재배열 부등식 - 작은 것은 작은 것끼리 큰 것은 큰 것끼리 붙여놓을 때 최대, 반대의 경우 최소가 됨
# 각 리스트를 정렬해서 (하나는 크기 순, 다른 하나는 크기의 역순), 대응하는 원소의 곱의 합

n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort(reverse=True)

print(sum(map(lambda i:a_list[i]*b_list[i], range(n))))     
