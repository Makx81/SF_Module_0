def game_core_v3(number):
    '''Устанавливаем random число, а потом уменьшаем или увеличиваем его по принципу деления отрезка в пропорциях золотого сечения 
       Функция принимает загаданное число и возвращает число попыток'''
    
    import math
    number = np.random.randint(1,101)
 
    count = 0
    a = 1                         #начальная граница отрезка
    b = 101                       #конечная граница отрезка
    phi = (1 + math.sqrt(5)) / 2  #пропорция золотого сечения


    while True:
        count += 1
        #расчитываем начальные точки деления
        x_1 = int(b - (b-a)/phi)   #точка x_1 делит отрезок (a, x_2) в отношении золотого сечения
        x_2 = int(a + (b-a)/phi)   #аналогично x_2 делит отрезок (b, x_1) в той же пропорции
        #проверяем попадание
        if number == x_1: 
            break                  #остановить выполнение цикла, если угадали число
        elif number == x_2: 
            break                  #остановить выполнение цикла, если угадали число
        elif number < x_1: 
            b = x_1                #поиск числа на сокращённом отрезке (a, x_1)
        elif number > x_2: 
            a = x_2                #поиск числа на сокращённом отрезке (b, x_2)
        else:                      #поиск числа на сокращённом отрезке (x_1, x_2)
            a = x_1
            b = x_2
    return(count)      #выход из цикла, если угадали
score_game(game_core_v3)