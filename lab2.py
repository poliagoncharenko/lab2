print('Флаг Швейцарии:')
print(u"\u001b[41m                              \u001b[0m")
print(u"\u001b[41m             \u001b[47;1m    \u001b[41m             \u001b[0m")
print(u"\u001b[41m       \u001b[47;1m                \u001b[41m       \u001b[0m")
print(u"\u001b[41m             \u001b[47;1m    \u001b[41m             \u001b[0m")
print(u"\u001b[41m                              \u001b[0m")
print()

print('Узор j:')
print('◯' * 2)
print()

print('Узор j:')
print(u"\u001b[47m \u001b[40m \u001b[47m  \u001b[40m \u001b[47m \u001b[0m")
print(u"\u001b[40m \u001b[47m \u001b[40m  \u001b[47m \u001b[40m \u001b[0m")
print(u"\u001b[47m \u001b[40m \u001b[47m  \u001b[40m \u001b[47m \u001b[0m")
print()

print('График функции y=x/3:')
print('↑ y')
for y in range(10, 0, -1):
    x = y * 3 -1
    print('|' + ' ' * x + '/')
print("/" + "-" * 10 * 3 + '→')
print('0' + ' ' * 10 *3 + 'x')
print()

print('Диаграмма процентного соотношения чисел от -3 до 3 и остальных:')
file = open('sequence.txt', 'r')
numbers = []
for number in file:
    numbers.append(float(number))
file.close()
count_3 = 0
count_else = 0
count_all = len(numbers)
for num in numbers:
    if -3 <= num <= 3:
        count_3+=1
    else:
        count_else+=1
percent3, percent_else = round(count_3/count_all * 100), round(count_else/count_all * 100)
point_3, point_else = u"\u001b[44m \u001b[0m" , u"\u001b[41m \u001b[0m"
print('   ↑ %')
for y in range(100, 0, -1):
    if y == 100:
        print(f'{y}|')
    elif 100 > y >= 10:
        if (percent3 >= y) and (percent_else >= y):
            print(f'{y} |{point_3}{point_else}')
        elif (percent3 >= y):
            print(f'{y} |{point_3}')
        elif (percent_else >= y):
            print(f'{y} | {point_else}')
        else:
            print(f'{y} |')
    # если не разделить, оно съезжает(
    else:
        if (percent3 >= y) and (percent_else >= y):
            print(f'{y}  |{point_3}{point_else}')
        elif (percent3 >= y):
            print(f'{y}  |{point_3}')
        elif (percent_else >= y):
            print(f'{y}  | {point_else}')
        else:
            print(f'{y}  |')