def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:                                 # x가 3의 배수가 아니면
            raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
        print(x)
    except Exception as e:                             # 함수 안에서 예외를 처리함
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise    # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김
 
try:
    three_multiple()
except Exception as e:                                 # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('스크립트 파일에서 예외가 발생했습니다.', e)
    
# 예외 - 내장된 예외 + 사용자 정의 예외
# class 예외이름(Exception):
  # def_init_(self):
    # super()._init_('에러메시지')

class NotTwoMultipleError(Exception):    # Exception을 상속받아서 새로운 예외를 만듦
    def __init__(self):
        super().__init__('2의 배수가 아닙니다.')
 
def two_multiple():
    try:
        x = int(input('2의 배수를 입력하세요: '))
        if x % 2 != 0:                     # x가 2의 배수가 아니면
            raise NotTwoMultipleError    # NotTwoMultipleError 예외를 발생시킴
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)
 
two_multiple()
