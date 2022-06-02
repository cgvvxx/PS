# PS & CP

> Problem Solving & Competitive Programming


## :muscle: Rule

- 코드 가독성을 위하여 변수명과 로직을 명확히 할 것

- 아이디어 도출 과정 및 간단한 코드 설명
- 시간복잡도, 공간복잡도 계산해 볼 것
- 같은 문제라도 다양한 방법으로 풀 수 있으면 시도
- 다른 사람의 풀이도 참고하여 더 좋은 아이디어 or 코드 짜는 법 참고하기

## :bulb: Convention

- 한 문제당 하나의 커밋

- 폴더는 문제 풀이 사이트 별로 구분할 것
- 파일명과 커밋 컨벤션은 다음과 같이 통일할 것
- 문제 풀이 플랫폼
  - programmers / boj / leetcode / codeforce
- 태그
  - solved : 정답을 맞춘 문제 제출
  - refactor : 이미 푼 문제에 대한 리팩토링, 다른 언어로 문제 재풀이
  - docs : 문서를 수정한 경우
  - chore : 그 외 자잘한 주석 변경 등

```
# {문제풀이플랫폼}_{문제번호}		- <파일명>

# {태그값}: [{문제번호}] - {문제이름}		- <커밋 메세지>
# {문제원본url}
# {알고리즘분류카테고리}
#
# 문제 풀이 관련 주석
# ...
# ps
# ...
```

```python
# e.g.
# boj_1753.py

# solved: [1753] 최단경로
# https://www.acmicpc.net/problem/1753
# graph-traversal, shortest-path, dijkstra
#
# 문제 풀이 관련 주석
# ...
# ps
# ...
```

## :computer: Algorithm Category

![Algorithm PS Roadmap](https://user-images.githubusercontent.com/82948893/158559705-17be3b9a-eb86-4cbe-8359-1da744ffc27f.png)

```markdown
algorithms
├── backtracking  :  백트래킹
├── bfs (breadth-first-search)  :  너비 우선 탐색
├── binary-search  :  이분 탐색
├── bitmask  :  비트마스킹
├── bruteforcing  :  완전 탐색
├── combinatorics  :  조합론
├── convex-hull  :  볼록 껍질
├── data-structure  :  자료 구조
├── dfs (depth-first-search)  :  깊이 우선 탐색
├── dijkstra  :  다익스트라
├── disjoint-set  :  분리 집합
├── divide-and-conquer  :  분할 정복
├── dp (dynamic-programming)  :  다이나믹 프로그래밍
├── euclidean-algorithm  :  유클리드 호제법
├── floyd-warshall  :  플로이드-워셜
├── geometry  :  기하학
├── graph-traversal  :  그래프 탐색
├── greedy  :  그리디
├── implementation  :  구현
├── inclusion-and-exclusion  :  포함 배제의 원리
├── knapsack  :  배낭 문제
├── lca (lowest-common-ancestor)  :  최소 공통 조상
├── mathematics  :  수학
├── mst (minimum-spanning-tree)  :  최소 스패닝 트리
├── number-theory  :  정수론
├── parsing  :  파싱
├── prefix-sum  :  누적 합
├── primality-test  :  소수 판정
├── priority-queue  :  우선순위 큐
├── queue  :  큐
├── recursion  :  재귀
├── regular-expression  :  정규 표현식
├── segment-tree  :  세그먼트 트리
├── shortest-path  :  최단 거리
├── sieve-of-eratosthenes  :  에라토스테네스의 체
├── sorting  :  정렬
├── stack  :  스택
├── string  :  문자열
├── topological-sorting  :  위상 정렬
├── tree  :  트리
├── trie  :  트라이
├── tsp (traveling-salesman-problem)  :  외판원 순회 문제
└── two-pointer  :  투 포인터
```

## :bookmark_tabs: Reference sites

- Programmers : https://programmers.co.kr/learn/challenges
- Backjoon : https://www.acmicpc.net/step 
- Leetcode : [https://leetcode.com](https://leetcode.com/)  
- Codeforce : [http://codeforces.com](http://codeforces.com/)

## :black_square_button: History

```NOW ~```

- 문제 풀이만 commit, 알고리즘 이론 정리는 모두 library repo로 이동

- 알고리즘 카테고리를 더 세분화하여 구분
- 커밋 컨벤션 맞추기

```~ 2022.03.15.```

- 매일 한 문제 이상 풀고 해당 문제 풀이에 대해 알고리즘 카테고리별로 그 날의 날짜로 커밋 메세지를 작성하여 정리
- ps 디렉토리에 이전 문제 풀이
