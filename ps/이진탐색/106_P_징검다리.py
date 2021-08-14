# Programmers - 징검다리
# Level 4
# 이진탐색


def is_possible(rocks, dist, n):
    
    before = 0
    rock_dist = 0
    count = 0
    
    for rock in rocks:
        
        rock_dist += rock - before
        
        if rock_dist >= dist:
            rock_dist = 0
            count += 1
            print(dist, rock)
            
        before = rock
    
    if count >= len(rocks) - n:
        return True
    else:
        return False
        

def solution(distance, rocks, n):
    
    rocks.sort()
    rocks.append(distance)
    max_dist = distance // (len(rocks) - n)
    min_dist = 1
    
    while min_dist <= max_dist:
        
        mid = (min_dist + max_dist) // 2
        
        if is_possible(rocks, mid, n):
            min_dist = mid + 1
        else:
            max_dist = mid - 1
    
    if is_possible(rocks, max_dist, n):
        return max_dist
    else:
        return mid
