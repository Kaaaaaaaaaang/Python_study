# try except else finally 사용
# try : 예외가 발생할 가능성이 있는 코드
# except : 예외가 발생했을 때 실행할 코드
# else : 예외가 발생하지 않았을 때 실행할 코드
# finally : 무조건 실행할 코드
try:
  number_input_a = int(input("정수입력 >> "))
  print("원의 반지름 : ", number_input_a)
  print("원의 둘레 : ", 2*3.14*number_input_a)
  print("원의 넓이 : ", 3.14*number_input_a*number_input_a)
except:
  print("정수를 입력하지 않았습니다.")
else:
  print("예외가 발생하지 않았습니다.")
finally:
  print("무조건 출력하는 문장입니다.")
# try 구문은 단독으로 사용할 수 없다. 반드시 except 구문 또는 finally 구문과 함께 사용해야 한다.
# else 구문은 반드시 except 구문 뒤에 사용해야 한다.
