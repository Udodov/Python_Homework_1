# 4. Напишите программу, которая по заданному номеру четверти, показывает
#  диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('enter the quarter number from 1 to 4 --> '))

if quarter == 1:
    print(f'The range of possible coordinates of points in {quarter} quarter: x > 0 and y > 0')
elif quarter == 2:
    print(f'The range of possible coordinates of points in {quarter} quarter: x < 0 and y > 0')
elif quarter == 3:
    print(f'The range of possible coordinates of points in {quarter} quarter: x < 0 and y < 0')
elif quarter == 4:
    print(f'The range of possible coordinates of points in {quarter} quarter: x > 0 and y < 0')
else:
    print('Incorrect input')