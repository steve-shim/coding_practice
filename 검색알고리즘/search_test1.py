from search_while import seq_search

number = 0
x = []  # 빈 리스트 x를 생성
# 리스트를 append 형식으로 추가하기 때문에 리스트의 크기가 정해지지 않아도 된다
while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))  # 배열 마지막에 원소를 추가
    number += 1

ky = float(input('검색할 값을 입력하세요.: '))  # 검색할 키 ky를 입력

idx = seq_search(x, ky)  # ky와 같은 값의 원소를 x에서 검색
if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')