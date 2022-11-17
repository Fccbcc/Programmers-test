## 풀이

def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    return sorted(answer)
  
  #해설 
  #정수형 isdigit()와 추가하는 함수인 .append를 쓴다.
