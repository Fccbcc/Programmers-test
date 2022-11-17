## 풀이

def solution(before, after):
    
    a = list(before)
    b = list(after)
    
    if sorted(a) == sorted(b):
        return 1
    else:
        return 0

def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0
