# # Создайте функцию генератор чисел Фибоначчи

number = int(input('Введите порядковое число Фибоначчи -> '))


def Fibon(number):
    sum_numbers = 0
    if number > 2:
        fibo = [0, 1]
        for i in range(0, number):
            sum_numbers = fibo[i] + fibo[i + 1]
            fibo.append(sum_numbers)
            yield sum_numbers, fibo
    else:
        print('Access denied')


test = iter(Fibon(number))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))

# def fact(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
#
#
# test = iter(fact(4))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
