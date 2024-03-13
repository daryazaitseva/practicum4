record1, record2, record3 = map(int, input('Введите рекорды игроков: ').split())
if record1 < record3 and record1 < record3:
    print(record3)
elif record1 < record2 and record3 < record2:
    print(record2)
else:
    print(record1)
