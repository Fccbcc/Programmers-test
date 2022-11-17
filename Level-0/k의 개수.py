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
