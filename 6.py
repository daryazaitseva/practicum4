score1, score2 = map(int, input('Введите счет двух команд ').split(':'))
if score1 > score2:
    print(1)
elif score1 == score2:
    print(0)
else:
    print(2)