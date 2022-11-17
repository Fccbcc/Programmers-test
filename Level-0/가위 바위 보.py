## 풀이

def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp
  
  #해설
  #여기서 주의할 점은 변환할때 같은 숫자가 되는걸 방지해 줘야 한다는 것!
