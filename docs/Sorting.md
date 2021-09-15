

# Sorting

## 정렬 알고리즘

> 주어진 리스트를 기준에 맞추어 정렬하여 출력하는 알고리즘

<br>

### 1. 정렬 알고리즘

- n개의 숫자가 입력으로 주어졌을 때, 이를 기준에 맞추어 정렬하여 출력하는 알고리즘

- 버블 정렬, 선택 정렬, 삽입 정렬, 병합 정렬, 퀵 정렬, 힙 정렬 등 다양한 정렬 종류가 있음

- Stable sort(안정 정렬) : 중복된 키의 순서를 바꾸지 않고 순서대로 정렬 알고리즘

  - stable : Bubble sort, Insertion sort, Merge sort, Counting sort
  - unstable : Selection sort, Quick sort, Heap sort

- In-place sort(제자리 정렬) : 추가적인 메모리 공간을 많이 혹은 전혀 필요로 하지 않는 정렬 알고리즘

  - in-place : Bubble sort, Selection, Insertion sort, Quick sort(?), Heap sort
  - not in-place : Merge sort, Counting sort

<p align="center"><img src=".\IMAGE\sorting.png" alt="adj" style="zoom:70%;" /></p>
<p align="center"><img src=".\IMAGE\sorting_2.gif" alt="adj" style="zoom:70%;" /></p>

<br>

#### 1. 버블 정렬(Bubble Sort)

- 구현 방식
  - 매번 이웃한 두 항을 비교하여 큰 값을 뒤로 정렬하는 방식
  - 처음으로 전체를 순회하는 경우 가장 큰 값이 맨 뒤에 저장됨
  - (전체 배열의 크기 - 현재까지 순회한 횟수) 만큼의 과정을 반복하여 정렬

- 구현이 단순, 시간복잡도는 항상 O(n^2), Stable, In-place

  - 같은 O(n^2)의 시간복잡도를 가지는 정렬에 비하여도 원소 비교시 평균 교환횟수가 평균적으로 더 많기 때문에 실질적으로 더 많은 시간 소요
  - 단, 각 라운드에서 원소를 비교할 때 교환이 이루어지지 않는 경우를 판단하는 변수를 설정하여 교환이 아예 이루어지지 않는 경우 종료함으로써 최선의 경우 시간복잡도를 O(n)으로 줄일 수 있음

  ```python
  def bubble_sort(arr):
  
      n = len(arr)
      
      for i in range(n-1):
          for j in range (n-1-i):
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]

<br>

#### 2. 선택 정렬(Selection Sort)

- 구현 방식

  - 주어진 배열 중에서 최솟값을 찾아 맨 앞에 위치한 원소와 교환
  - 맨 앞에 원소를 제외한 나머지 리스트에 대해서 위의 과정을 반복
  - 하나의 원소가 남을 때 까지 위의 과정을 반복

- 구현이 단순, 시간복잡도는 항상 O(n^2), Unstable, In-place

  - 정렬을 위한 비교횟수는 많으나 교환 횟수는 적음

  ```python
  def selection_sort(arr):
  
      n = len(arr)
  
      for i in range(0, n-1):
          least = i
          for j in range (i+1, n):
              if arr[least] > arr[j]:
                  least = j
          arr[i], arr[least] = arr[least], arr[i]
  ```

<br>

#### 3. 삽입 정렬(Insertion Sort)

- 구현 방식

  - 앞에서부터 차례대로 이미 정렬된 앞의 배열과 비교하여 자신의 위치를 찾아 삽입하여 정렬하는 방법
  - 두 번째 원소부터 앞의 자료와 비교하여 크기가 작은 경우 첫 번째 자리로, 큰 경우 그대로 정렬
  - 세 번째 원소부터 같은 방법으로 앞의 배열에서 자기보다 크기가 작은 원소가 있는 자리로 삽입하여 정렬하는 과정으 반복

- 평균 시간복잡도 O(n^2), Stable, In-place

  - 대부분이 정렬되어 있는 경우가 최선으로 시간복잡도는 O(n)
  - 반대로 역순으로 정렬되어 있는 경우가 최악으로 시간복잡도는 O(n^2)

  ```python
  def insertion_sort(arr):
  
      n = len(arr)
  
      for i in range(1, n):
          key = arr[i]
          j = i-1
          while j >= 0 and arr[j] > key:
              arr[j+1] = arr[j]
              j = j-1
          arr[j+1] = key
  ```

<br>

#### 4. 병합 정렬(Merge Sort)

- 분할 정복(Divide and conquer) 알고리즘의 방법 중 하나

- 구현 방식

  - 리스트의 길이가 0 이나 1인 경우 정렬되었다고 간주
  - 정렬 되지 않은 리스트의 경우 절반으로 잘라 두 부분 리스트로 나눔
  - 각 부분 리스트를 재귀적으로 병합 정렬을 이용하여 정렬하는 과정을 반복
  - 부분 리스트를 하나의 정렬된 리스트로 병합 - merge 하는 과정에서 실제 정렬이 이루어짐

- 평균 시간복잡도 O(nlogn), 공간복잡도 O(n), Stable, not In-place

  - 데이터의 분포에 상관 없이 정렬하는 시간은 O(nlogn)으로 동일
  - 연결리스트(Linked list)를 이용하는 경우 in-place sorting을 구현할 수 있음

  ```python
  def merge_sort(arr):
      
      def merge(left, right):
      
          sorted_list = []
          while len(left) > 0 or len(right) > 0:
          
              if len(left) > 0 and len(right) > 0:
                  if left[0] <= right[0]:
                      sorted_list.append(left[0])
                      left = left[1:]
                  else:
                      sorted_list.append(right[0])
                      right = right[1:]
                      
              elif len(left) > 0:
                  sorted_list.append(left[0])
                  left = left[1:]
                  
              elif len(right) > 0:
                  sorted_list.append(right[0])
                  right = right[1:]
                  
          return sorted_list
  
      n = len(arr)
      
      if n <= 1:
          return arr
          
      else:
          mid = n // 2 
          left = merge_sort(arr[:mid])
          right = merge_sort(arr[mid:])
          return merge(left, right)
  ```

<br>

#### 5. 퀵 정렬(Quick Sort)

- 분할 정복(Divide and conquer) 알고리즘의 방법 중 하나, 병합 정렬과 달리 리스트를 비균등 분할

- 구현 방식

  - 리스트의 한 원소(pivot)을 선택
  - 피봇을 기준으로 피봇보다 작은 요소는 왼쪽으로, 피봇보다 큰 요소는 오른쪽으로 옮김
  - 피봇을 제외한 왼쪽 리스트와 오른쪽 리스트를 위와 같은 방법으로 정렬하는 과정을 반복

- 평균 시간복잡도 O(nlogn), 공간복잡도 O(logn), Unstable, In-place

  - 일반적으로 속도가 빠르고 추가 메모리 공간을 적게 사용
  - 정렬된 리스트에서는 비균등 분할로 인해 오히려 시간이 오래 걸림
  - 리스트가 계속 불균형하게 나누어지는 경우(피봇이 양 끝값 중 하나가 선택되는 경우) 최악으로 시간복잡도 O(n^2)

  ```python
  #1. 재귀함수를 이용, 새로운 리스트를 생성하므로 추가적인 메모리 사용
  def quick_sort(arr):
  
      n = len(arr)
      
      if n <= 1:
          return arr
          
      else:
          pivot = arr[n // 2]
          lesser_arr, equal_arr, greater_arr = [], [], []
          
          for num in arr:
              if num < pivot:
                  lesser_arr.append(num)
              elif num > pivot:
                  greater_arr.append(num)
              else:
                  equal_arr.append(num)
                  
          return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
      
      
  #2. in-place 형태의 퀵 정렬
  def quick_sort(arr):
      
      def sort(low, high):
      
          if high <= low:
              return
  
          mid = partition(low, high)
          sort(low, mid - 1)
          sort(mid, high)
  
      def partition(low, high):
      
          pivot = arr[(low + high) // 2]
          
          while low <= high:
              while arr[low] < pivot:
                  low += 1
              while arr[high] > pivot:
                  high -= 1
              if low <= high:
                  arr[low], arr[high] = arr[high], arr[low]
                  low, high = low + 1, high - 1
          return low
  
      return sort(0, len(arr) - 1)
  ```

<br>

#### 6. 힙 정렬(Heap Sort)

- 최대 힙 트리 혹은 최소 힙 트리(완전 이진 트리)를 이용하여 정렬하는 방법

- 구현 방식

  - 주어진 리스트를 최대 힙으로 만듦
  - 하나의 원소씩 힙에서 꺼내어 배열의 마지막부터 차례대로 저장

- 시간복잡도 O(nlogn), Unstable, In-place

  - 항상 시간복잡도가 O(nlogn)으로 속도가 빠르고 추가 메모리 사용이 없음
  - 같은 시간복잡도 O(nlogn) 정렬보다는 실제 정렬되는 시간은 느림

  ```python
  def heap_sort(arr):
    
      def heapify(unsorted, index, heap_size):
      
          largest = index
          left_index = 2 * index + 1
          right_index = 2 * index + 2
          
          if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
              largest = left_index
          if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
              largest = right_index
          if largest != index:
              unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
              heapify(unsorted, largest, heap_size)
          
      n = len(arr)
      mid = n // 2
      for i in range(mid-1, -1, -1):
          heapify(arr, i, n)
      
      for i in range(n-1, 0, -1):
          arr[0], arr[i] = arr[i], arr[0]
          heapify(arr, 0, i)
  ```

<br>

#### 7. 계수 정렬(Counting Sort)

- 두 수를 비교해서 정렬하는 비교 정렬이 아닌 각 원소의 등장 횟수를 세서 정렬하는 방법

- 구현 방식

  - 배열 내 원소의 최댓값 K에 대하여 K+1의 counting 배열을 생성
  - 배열을 순회하면서 각 원소에 해당하는 인덱스에 counting 배열 값을 1씩 증가시키고 이를 누적합으로 변환
  - 배열의 마지막 인덱스부터 순회하면서 인덱스에 해당하는 counting 배열 값의 위치에 원소를 저장하고 couting 배열 값을 1씩 감소시킴

- 시간복잡도 O(n+k), 공간복잡도 O(k), Stable, not In-place

  - 정수로 표현할 수 있는 자료에 대해서만 적용이 가능
    - 정렬할 값이 양의 정수이고, 주어진 자료의 범위를 알고 있는 경우 사용
  - 배열 내 원소의 최댓값이 K에 대해 K+1의 길이를 가진 Counting 배열이 필요함, 따라서 K의 값이 클수록 비효율적인 정렬

  ```python
  def counting_sort(arr):
  
      K = max(arr)
      n = len(arr)
      counts = [0] * (K + 1)
      
      for num in arr:
          counts[num] += 1
  
      for c in range(1, len(counts)):
          counts[c] += counts[c - 1]
  
      sorted_arr = [0] * n
      for n in range(n - 1, -1, -1):
          sorted_arr[counts[arr[n]] - 1] = arr[n]
          counts[arr[n]] -= 1
  
      return sorted_arr
  ```

