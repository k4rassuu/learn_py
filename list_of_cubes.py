# List of cubes
# Coded by Martynov V.


# Создаем cписок и две пустые переменные для работы с ними
list_cubed = []
var1 = 0
var2 = 0
# ---------------------------------------------------------

for i in range(1, 1001, 2):             # Создаем список нечетных чисел 1 - 1000
    cubed = i ** 3                      # Возводим ((i) - каждый элемент списка) в куб
    list_cubed.append(cubed)            # заносим полученые значения в пустой лист
    summa = 0                           # Временная переменная для работы в цикле
    for _i in str(cubed):               # Теперь складываем сумму цифр чисел...
        summa += int(_i)
    if summa % 7 == 0:                  # ...и создаем условие при котором они будут записаны в список
        var1 += cubed

    summa2 = 0                          # Вторая временная переменная
    for _i in str(cubed + 17):          # К каждому числу прибавляем 17...
        summa2 += int(_i)

    if summa2 % 7 == 0:                 # ...и создаем условие при котором они будут записаны в список
        var2 += cubed

print("Ответ на первое задание : ", var1)
print("Ответ на второе задание : ", var2)
