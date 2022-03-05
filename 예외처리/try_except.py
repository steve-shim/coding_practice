# input('인덱스와 나눌 숫자를 입력하세요: ').split()
# ['5', '2']
# map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
# <map object at 0x000001F3F424D348>
# list(map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split()))
# [5, 2]

y = [10, 20, 30]

while True:
    try:
        index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
        print(y[index] / x)
        break

    except ZeroDivisionError as e:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
        print('숫자를 0으로 나눌 수 없습니다.', e)
    except IndexError as e:           # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
        print('잘못된 인덱스입니다.', e)
    except Exception as e:            # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
        print('예외 발생', e)    
    print("재입력!")
    continue