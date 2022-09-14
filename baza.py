import random
import time


HELP = '''
помощь - помощь с коммандами
запись - записать нового пользователя
поиск - поиск по ID
поиск по фамилии - поиск по фамилии
завершение - завершение сеанса
'''

about=[]
while 2==2:
    c = input('Введите команду: ')
    if c == 'запись':
        file = open('baza.txt', 'a')
        id = ''
        for i in range(6):
            id = str(id) + str(random.randint(0, 9))
            
        
        last_name = input('Введите Вашу фамилию: ')
        name = input('Введите Ваше имя: ')
        otch = input('Введите Ваше отчество: ')
        while 1 ==1 :
            age = input('Введите Вашу дату рождения(д.м.г): ')
            if len(age)!= 10:
                print('Дата рождения введена некорректно! Попробуйте ещё раз!')
            else:
                break
        while 1==1:
            num=input('Введите Ваш номер телефона(+7(XXX)-XXX-XX-XX) или поставьте тире: ')
            if len(num)!= 17 and num != '-':
                print('Номер телефона введён некорректно! Попробуйте ещё раз!')
            else:
                break
        about.append(name)
        about.append(last_name)
        about.append(otch)
        about.append(num)
        about.append(age)
        print('Записано!')
        print('Ваш id: ' + id)
        file.write(str(id) + '\n' + str(about) + '\n')
        time.sleep(1)
        file.close()
        about=[]
    elif c == 'поиск':
        filer = open('baza.txt', 'r')
        file_r = filer.read()
        file_rs = file_r.split('\n')
        k = input('Введите Ваш id: ')
        if k in file_rs:
            i = int(file_rs.index(k) + 1)
            out = file_rs[int(i)]
            out = out.replace('[', '').replace(']', '').replace("'", "")
            out_s = out.split(' ')
            name1 = out_s[0].replace(',', '')
            last = out_s[1].replace(',', '')
            otch1 = out_s[2].replace(',', '')
            num = out_s[3].replace(',', '')
            data = out_s[4].replace(',', '')
            print('Имя: ' + name1)
            print('Фамилия: ' + last)
            print('Отчество: ' + otch1)
            print('Дата рождения: ' + data)
            print('Номер телефона: ' + num)
            
        else:
            print('Нет такого id!')
        filer.close()
        
        
    elif c == 'поиск по фамилии':
        name1 = 'p'
        filer = open('baza.txt', 'r')
        file_r = filer.read()
        file_rs = file_r.split('\n')
        n = input('Введите фамилию: ')
        b = int(1)
        k = int(0)
        for i in range(len(file_rs)):
            k = k+1
            if i == 0:
                k = int(i)
            if i%2 != 0:
                ch = file_rs[k]
                ch = ch.replace('[', '').replace(']', '').replace("'", "")
                ch_s = ch.split(', ')
                if n in ch_s:
                    name1 = ch_s[0].replace(',', '')
                    last = ch_s[1].replace(',', '')
                    otch1 = ch_s[2].replace(',', '')
                    numm = ch_s[3].replace(',', '')
                    data = ch_s[4].replace(',', '')
                    f = file_rs[k-1]
                    print(str(b) + '.'+ ' '+ 'Имя: ' + name1)
                    print('   '+'Фамилия: ' + last)
                    print('   '+'Отчество: ' + otch1)
                    print('   '+'Дата рождения: ' + data)
                    print('   '+'Номер телефона: ' + numm)
                    print('   '+'ID: ' + f)
                    b=b+1
                    file_rs.remove(file_rs[k])
                    file_rs.remove(f)
                    k = k-2


        if name1 == 'p':
            print('Нет такого пользователя!')
        filer.close()
    
    elif c == 'очистка базы':
        cvc=input('Введите код: ')
        if cvc == '0504':
            fileo=open('baza.txt', 'w')
            fileo.write('')
            fileo.close()
            print('База данных очищена!')
        else:
            print('Неверный код!')

    elif c == 'помощь':
        print(HELP)

    elif c== 'завершение':
        print('Спасибо за использование! До свидания!')
        time.sleep(1)
        break
        
    else:
        print('Неизвестная команда!')

