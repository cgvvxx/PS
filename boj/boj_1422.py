# solved: [1422] 숫자의 신
# https://www.acmicpc.net/problem/1422
# sorting
# 
# Platinum 4
# 프로그래머스 level 2 - 가장 큰 수(https://programmers.co.kr/learn/courses/30/lessons/42746)와 비슷한 문제 (프로그래머스에서는 level2 ??)
# 기본적으로 길이가 긴 원소가 많을 수록 숫자가 커짐
# 1번째 sort => 1. 길이순, 2. 크기순
# 길이가 길고, 크기가 가장 큰 원소가 n-k개 더 추가됨
# * 2번째 sort => 해당 숫자를 연달아 적었을 때 큰 숫자 순 (문제에서 최대 10개로 이루어진 숫자이므로 (x*10)[:10]으로 슬라이싱)
# sort된 숫자들을 연달아 print
# 어떻게 두 번째 sort를 할 것인지 생각하는게 굉장히 어려웠던 문제

k, n = map(int, input().split())
nums = [input() for _ in range(k)]

nums.sort(key=lambda x:(len(x), x))
nums = nums + [nums[-1]] * (n-k)
nums.sort(key=lambda x:int((x*10)[:10]) , reverse=True)

print(''.join(nums))
