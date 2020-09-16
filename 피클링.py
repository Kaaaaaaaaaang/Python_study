# 피클링(pickling) = 파이썬 객체를 파일에 저장하는 과정
# 언피클링(unpickling) = 파일에서 객체를 읽어오는 과정

import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean' : 90, 'englisg' : 95, 'mathmatics' : 85, 'science' : 82}

with open('james.p', 'wb') as file:
    # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)


with open('james.p', 'rb') as file:
    # james.p 파일은 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)
