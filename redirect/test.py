'''
cd redirect
python test.py 2> err.txt 1> out.txt
'''
import traceback
import sys

number = 0
x = []  # 빈 리스트 x를 생성
# 리스트를 append 형식으로 추가하기 때문에 리스트의 크기가 정해지지 않아도 된다
while number <= 10:
    try:
        if number%2 == 0:
            raise ValueError('Even Err')
        assert number!=5, '5 Err'
        
        x.append(float(number))
        print(x)
    except Exception as e:
        traceback.print_exc()
    # except Exception as e:
    #     print(e, file=sys.stderr)
    number += 1
