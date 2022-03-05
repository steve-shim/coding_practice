'''
예외를 발생시키는 예외처리랑 비슷하지만, 
예외처리는 에러가 발생했을때 어떤 처리를 하기위한 코드이고, 
assert (가정 설정문)은 어떤 조건이 True임을 보증하기 위해서 사용하는 것 입니다.
raise는 만약에 오류가 발생했을때 "except 와 함께 이렇게 처리해라" 는 뜻

assert [조건], [오류메시지]
assert는 이 조건이 참일때 코드는 내가 보장한다. 이 조건은 올바르다!
하지만 이 조건이 거짓이라는 것은 내가 보증하지 않은 동작이다. 
그러니 AssertionError를 발생해라.

'''
try:
    name = "2BlockDMask"
    age = int(input("나이 입력 : "))
    assert age >= 0, '나이가 마이너스인게 가능한가 휴먼?'
    assert name[0].isalpha(), '대문자로 시작하지 않습니다'
except Exception as e:
    print(e) # 이름이 대문자로 시작하지 않습니다
