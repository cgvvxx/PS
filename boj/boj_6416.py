# solved: [6416] 트리인가?
# https://www.acmicpc.net/problem/6416
# tree
#
# Gold 5
# 1. 들어오는 간선이 하나도 없는 루트 노드가 하나인지 check
# 2. 루트 노드를 제외한 모든 노드는 단 하나의 들어오는 간선만 가지고 있는지 check
# 3. 이 때 노드가 없는 경우 tree임을 check 해야함

from collections import defaultdict


def is_tree(idx, ies, ns):
    
    if not ns:
        print(f'Case {idx} is a tree.')
        return

    check = ns - set(ies.keys())
    if len(check) != 1:
        print(f'Case {idx} is not a tree.')
        return
    
    for e in ies:
        if len(ies[e]) != 1:
            print(f'Case {idx} is not a tree.')
            return
    
    print(f'Case {idx} is a tree.')


inbound_edges = defaultdict(list)
nodes = set()
idx = 1
flag = False

while True:

    if flag:
        break
    
    line = input()

    if not line:
        continue
    else:
        for s in line.split('  '):
            a, b = map(int, s.split())

            if a == b == -1:
                flag = True
                break  
            elif a == b == 0:
                is_tree(idx, inbound_edges, nodes)
                
                inbound_edges = defaultdict(list)
                nodes = set()
                idx += 1
            else:
                nodes.add(a)
                nodes.add(b)
                inbound_edges[b].append(a)
