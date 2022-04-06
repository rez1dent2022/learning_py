print("Урок №1")
#  Задание 1: Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные,
# затем выведите на экран.
#
# Работа с переменными и их типом
sec = 15.5
print(sec)
print(type(sec))

receipt = 2000000000
print(receipt)
print(type(receipt))

costs = 1800000000
print(costs)
print(type(costs))

shtat = 23
print(shtat)
print(type(shtat))

receipt_1 = "Оборот ="
print(type(receipt_1))
print(receipt_1, receipt)

# Запрос данных у пользователя.
# print("Введите имя") #Первый вариант запроса
name = input("Ведите имя: ")
age = input("Введите ваш возраст: ")
print(name,":",age,"лет (года)")
print("*"*40)


# Задание 2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
# print("Введите количество секунд") #Первый вариант запроса

sec_2 = input("Введите количество секунд: ")
sec_2 = int(sec_2)
hour = (sec_2 // 3600)
min = (sec_2 // 60 % 60)
sec_left = (sec_2 % 60 % 60)
dp = ":"
print(hour)
print(min)
print(sec_left)
hour = str(hour)
min = str(min)
sec_left = str(sec_left)
print(hour + dp + min + dp + sec_left)
print("*"*40)

# Задание 3 Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
# print("Введите число")  #Первый вариант запроса
n = input("Введите число: ")
nn = (n+n)
nnn = (n+n+n)
n = int(n)
nn = int(nn)
nnn = int(nnn)
rez = (n+nn+nnn)
print(n,nn,nnn)
print(rez)
print("*"*40)

# Задание 4 Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
i = int(input("Введите число: "))
k = - 1
while i > 10:
    d = i % 10
    i //= 10
    if d > k:
       k = d
print(k)
# Задание №5
dohod = input("Введите доход: ")
cost = input("Введите расход: ")
dohod = int(dohod)
cost = int (cost)
if dohod> cost:

    print("Прибыль- выручка больше издержек")
else:
    print("Убыток - выручка меньше издержек")
prib = dohod - cost
if prib > 1:
    rent = prib/dohod
    print('Ваша рентабельность =', rent)
    sotr = int(input('Введите количество сотрудников: '))
    print ("Ваша прибыль на сотрудника составляет: ", prib/sotr)
else:
    print('У вас все получится в следующий раз!')
