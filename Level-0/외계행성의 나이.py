#풀이

def solution(age):
    answer = ''
    pro = ['a','b','c','d','e','f','g','h','i','j']
    for i in str(age):
        answer += pro[int(i)]
    return answer
 
#풀이
#str -> 한글자씩 뽑아올 수 있음
