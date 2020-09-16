# 파일객체 = open(파일이름, 파일모드)
# 파일객체.write('문자열')
# 파일객체.close()

file = open('hello.txt', 'w')
# hello.txt 파일을 쓰기모드(w)로 열기. 파일 객체 반환
file.write('Hello, world!')
# 파일에 문자열 저장
file.close()
# 파일 객체 닫기

# 파일에서 문자열 읽기
# 변수 = 파일객체.read()
file = open('hello.txt', 'r')
# hello.txt 파일을 읽기모드(r)로 열기. 파일 객체 반환
s = file.read()
# 파일에서 문자열 읽기
print(s)
file.close()
# 파일 객체 닫기

# 자동으로 파일 객체 닫기
# with open(파일이름, 파일모드) as 파일 객체:
#   코드
with open('hello.txt', 'r') as file:
# hello.txt 파일을 읽기모드(r)로 열기
    s = file.read()
    # 파일에서 문자열 읽기
    print(s)

# 반복문으로 문자열 여러 줄을 파일에 쓰기
with open('hello.txt', 'w') as file:
    # hello.txt 파일을 쓰기 모드(w)로 열기
    for i in range(3):
        file.write('Hello, world!{0}\n'.format(i))

# 리스트에 들어있는 문자열을 파일에 쓰기
# 파일객체.writelines(문자열리스트)
lines = ['안녕하세요\n', '파이썬\n', '공부중입니다.\n']
with open('hello.txt', 'w') as file:
    # hello.txt 파일을 쓰기모드(w)로 열기
    file.writelines(lines)

# 파일의 내용을 한 줄씩 리스트로 가져오기
# 변수 = 파일객체.readlines()
with open('hello.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# 파일의 내용을 한 줄씩 읽기
# 변수 = 파일객체.readline()
with open('hello.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line.strip('\n'))
        # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
# readline으로 파일을 읽을 때는 while 반복문을 활용해야 한다.
# 파일에 문자열이 몇 줄이나 있을지 모르기 때문에
# while은 특정 조건이 만족할 때 계속 반복하므로 파일의 크기에 상관없이 문자열을 읽어올 수 있다.

# for 반복문으로 파일의 내용을 줄 단위로 읽기
with open('hello.txt', 'r') as file:
    for line in file:
        # for에 파일 객체를 지정하면 파일의 내용을 한줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))
        # 파일에서 읽어노 문자열에서 \n 삭제하여 출력
        
