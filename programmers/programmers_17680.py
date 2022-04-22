# solved: [17680] 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680
# implementation
#
# Level 2
# cache, cache_num이라는 dictionary를 만들어 순서 체크
# cache는 각 도시를 key, 순서를 value
# cahce_num은 순서를 value, 도시를 key
# city가 cache에 있으면 ans += 1 없으면 ans += 5 & cacheSize를 넘는 경우에만 가장 작은 값을 가지는 city를 pop

def solution(cacheSize, cities):
    
    if cacheSize == 0:
        return len(cities) * 5
    
    cache = dict()
    cache_num = dict()
    ans, idx = 0, 0
    
    for city in cities:
        
        city = city.lower()
        idx += 1
        
        if city in cache:
            ans += 1
            
        else:
            ans += 5
            
            if len(cache) >= cacheSize:
                tar = cache_num[min(cache.values())]
                cache.pop(tar)
    
        cache[city] = idx
        cache_num[idx] = city
        
    return ans
