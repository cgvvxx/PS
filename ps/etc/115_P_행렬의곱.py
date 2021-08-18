# Programmers - 행렬의 곱
# Level 2


def solution(arr1, arr2):
    
    def inner_product(arr1, arr2):
    
        inner_sum = 0
        for a1, a2 in zip(arr1, arr2):
            inner_sum += a1*a2

        return inner_sum
    
    arr2 = list(zip(*arr2))
    
    return [[inner_product(row, col) for col in arr2] for row in arr1]            