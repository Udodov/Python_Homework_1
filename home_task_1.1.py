# 1. Напишите программу, которая принимает на вход цифру, обозначающую
#  день недели, и проверяет, является ли этот день выходным.
#   Пример:
#  6 -> да
#  7 -> да
#  1 -> нет

number = int(input('Enter a positive integer from 1 to 7: '))
if (number >= 1) and (number <= 7):
    if (number >= 6) and (number <= 7):
        print('Hurray!!! Day off!!!')
    else:
        print('we need to work...:(')
else:
    print('Please enter a number from 1 to 7!')
