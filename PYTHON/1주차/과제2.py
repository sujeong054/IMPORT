# 랜덤함수
#from random import *
# print(random()) 0~1.0 미만의 임의의 값 생성
# print(random() * 10) 0~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10)) 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10) + 1) 1 ~ 10 미만의 임의의 값 생성
# print(randrange(1, 46)) 1 ~ 46 미만의 임의의 값 생성
# print(randint(1, 46)) 1 ~ 45 미만의 임의의 값 생성



from random import *

date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")