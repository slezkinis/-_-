import time


while 1==1:
    r=int(input('Я могу определить твой возраст. Введите, в каком году вы родились: '))
    for i in range(4):
        print(f'Идёт подсчёт{(i+1) * "."}')
        time.sleep(0.3)
    print('Мне удалось посчитать ваш возраст')
    print(f'Вам: {2022-r}')
    time.sleep(1)
    break
