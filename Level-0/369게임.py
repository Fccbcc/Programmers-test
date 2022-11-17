## 풀이

def solution(order):
    answer = 0
    
    for i in str(order):
        if int(i)!=0 and int(i)%3==0:
            answer += 1
    return answer

# 해설
# 배수에서 주의해야하는 부분.. 0을 나누면 0이다
