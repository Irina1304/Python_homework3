#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

list_ = input('Введите последовательность положительных чисел через пробел: ')
result_list = [int(i) for i in list_.split(' ') if i.isdigit()]

list2 = []
number = int(len(result_list))

for i in range(len(result_list)):
    while i < len(result_list)/2 and number > len(result_list)/2:
        number = number - 1
        a = result_list[i] * result_list[number]
        list2.append(a)
        i += 1

print(result_list)
print(list2)