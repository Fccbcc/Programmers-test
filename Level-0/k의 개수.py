## 풀이

def solution(i, j, k):
    answer = 0
    tae = []
    for a in range(i,j+1):
        for b in str(a):
            if b==str(k):
                tae.append(b)
    answer = len(tae)            
    return answer
  
#해설 생략(합성수 찾기와 유사)

#다른 풀이

def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer


def solution(i, j, k):
    answer = 0
    for num in range(i, j + 1):
        if str(k) in str(num):
            answer += str(num).count(str(k))
    return answer
