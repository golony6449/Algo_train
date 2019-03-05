case = int(input())

# 마지막 날
cal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for idx in range(case):
    # 입력 and 파싱
    input_s = input()
    year = int(input_s[:4])
    month = int(input_s[4:6])
    day = int(input_s[6:])

    # 범위 검증
    if month >= 1 and month <= 12:
        if day <= cal[month]:
            print('#{} {:04d}/{:02d}/{:02d}'.format(idx + 1, year, month, day))
        else:
            print('#{} -1'.format(idx+1))
    else:
        print('#{} -1'.format(idx+1))
