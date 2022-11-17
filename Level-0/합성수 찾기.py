## 풀이

def solution(n):
    answer = 0
    tae=[]
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i%j==0:
                tae.append(i)
        if tae.count(i)>=3:
            answer += 1
        
    return answer
  
  # 해설
  # 합성수의 개념과 range의 개념을 이용해서 푼다(range 안에 무조건 약수가 존재하니까)
