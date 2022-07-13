# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).
# Пример:
#  x=34; y=-30 -> 4
#  x=2; y=4-> 1
#  x=-34; y=-30 -> 3

def quarter(abscissa, ordinate):
    if (abscissa > 0) and (ordinate > 0):
        print('I quarter')
    elif (abscissa < 0) and (ordinate > 0):
        print('II quarter')
    elif (abscissa < 0) and (ordinate < 0):
        print('III quarter')
    elif (abscissa > 0) and (ordinate < 0):
        print('IV quarter')


abscissa = float(input('Enter coordinates (x): '))
ordinate = float(input('Enter coordinates (y): '))

if abscissa == 0 and ordinate == 0:
    print('The point is located in the center of the coordinate system. The coordinate must not be = 0')
elif ordinate == 0:
    print('The point is located on the ordinate axis. The coordinate must not be = 0')
elif abscissa == 0:
    print('The point is located on the abscissa axis. The coordinate must not be = 0')
else:
    quarter(abscissa, ordinate)
