# Programmers - 가장 큰 수
# Level 2
# 정렬

def compare(a, b):
    # 3, 30, 34의 크기 비교는 34 > 3 > 30
    # 이는 3333, 3030, 3434의 크기 비교랑 같음!

    a = int((str(a) * 4)[:4])
    b = int((str(b) * 4)[:4])

    if a >= b:
        return True
    else:
        return False


def quick_sort(arr, low, high):
    if low >= high:
        return

    pivot = low
    left = low + 1
    right = high

    while left <= right:
        while left <= high and compare(arr[left], arr[pivot]):
            left += 1
        while right > low and compare(arr[pivot], arr[right]):
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort(arr, low, right - 1)
    quick_sort(arr, right + 1, high)


def solution(numbers):
    quick_sort(numbers, 0, len(numbers) - 1)

    return str(int(''.join(list(map(str, numbers)))))


# sort의 key를 이용하면 간단히 할 수 있음!
def solution(numbers):
    numbers.sort(key=lambda x:int((str(x)*4)[:4]), reverse=True)
    return str(int(''.join(list(map(str, numbers)))))