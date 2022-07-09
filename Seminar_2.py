# Задача 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

ls = list(input('Введите массив - '))

def max(a):
    maxnum = a[0]
    for i in a:
        if(maxnum<i):
            maxnum = i
    return maxnum

print(f'Результ - {max(ls)}')


# def get_max(a,b,c,d,e):
#     result = max([a,b,c,d,e])
#     return result

# res = get_max(5,25,6,32,5) 
# print(res)