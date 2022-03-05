try: 
    a = int(input("1~5 까지 숫자 입력(3입력 불가) : ")) # 범위를 벗어나면 error 발생! 
    if a < 1 or a > 5: 
        raise ValueError('ㅎ')
    elif a==3:
        raise Exception('Bye')  
    print(f"입력한 a : {a} 입니다.") # 범위 안에 있으면 정상 출력
except ValueError as e: 
    print("1~5 사이 입력하라고 했잖아요.", e)
except Exception as e: 
    print("3입력", e)

