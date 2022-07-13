# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#   Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

x_1 = float(input('Enter the coordinate of point A(x1): '))
y_1 = float(input('Enter the coordinate of point A(y1): '))
x_2 = float(input('Enter the coordinate of point B(x2): '))
y_2 = float(input('Enter the coordinate of point B(y2): '))

print('Distance between points A and B =', round(((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** 0.5, 2))