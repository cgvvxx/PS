# Baekjoon 1541
# Silver 2
# 그리디

eq = input()
try:
    eq.index("-")
    res = 0
    for i, sen in enumerate(eq.split("-")):
        if i == 0:
            for nums in sen.split("+"):
                res += int(nums)
        else:
            part_res = 0
            for nums in sen.split("+"):
                part_res += int(nums)
            res -= part_res
    print(res)
except:
    res = 0
    for nums in eq.split("+"):
        res += int(nums)
    print(res)
