question1 = input('Собака короткошерстой породы? ').lower()
if question1 == 'да':
    question2 = input('Рост собаки менее 50 см? ').lower()
    if question2 == 'да':
        question3 = input('У собаки короткий хвост? ').lower()
        if question3 == 'да':
            print('Это английский бульдог')
        else:
            question4 = input('У собаки длинные уши? ').lower()
            if question4 == 'да':
                print('Это гончая')
            else:
                question5 = input('У собаки короткое тело?').lower()
                if question5 == 'да':
                    print('Это мопс')
                else:
                    print('Это чихуахуа')
    else:
        question3 = input('Собака весит более 50 кг? ').lower()
        if question3 == 'да':
            print('Это датский дог')
        else:
            print('Это фоксхаунд')
else:
    question2 = input('Рост собаки менее 50 см? ').lower()
    if question2 == 'да':
        question3 = input('У собаки доброжелательный характер? ').lower()
        if question3 == 'да':
            print('Это кокер-спаниель')
        else:
            print('Это ирландский сеттер')
    else:
        question3 = input('У собаки рост менее 70 см? ').lower()
        if question3 == 'да':
            question4 = input('У собаки длинные уши? ').lower()
            if question4 == 'да':
                print('Это большой вандейский грифон')
            else:
                print('Это колли')
        else:
            question4 = input('Окрс рыжий  белыми отметинами? ').lower()
            if question4 == 'да':
                print('Это сенбернар')
            else:
                question5 = input('Белоснежный окрас?').lower()
                if question5 == 'да':
                    print('Это ирландский олкодав')
                else:
                    print('Это ньюфаундленд')

