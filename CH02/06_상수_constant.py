#06_상수_constant.py

# 상수
# 프로그램 진행 중 값이 변경되지 않는 저장소(개념)

# 파이썬에서는 별도의 상수가 없음

# 변수와 구분하기 위해 대문자로 사용할 뿐
# 나중에 상수의 값을 변경해도 오류 없음

# PI = 3.141592
# TAX_RATE = 0.35

# 원의 넓이를 계산해보자.

PI = 3.141592 # 고정값이므로 대문자를 이용해 상수 표시

r = 10

area = r * r * PI
print(area)

######################################################################

#이자율이 3% 인 은행의 예금액을 계산하는 계산식 프로그램을 작성
INT_RATE = 0.03

deposit = 10000

interest = deposit * INT_RATE # 정수 * 실수 연산이므로 결과는 실수로 변환
balance = deposit + interest

print(balance)
print(int(balance)) # 정수형으로 반환

# 천단위 구분기호 사용 : format 함수 사용
print(format(int(balance), ','))
