# 2. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def expression(x, y, z):
    print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} will be {(not (x or y or z)) == (not x and not y and not z)}')
    return (not (x or y or z)) == (not x and not y and not z)


if (expression(0, 0, 0) and expression(0, 1, 0) and
        expression(0, 0, 1) and expression(0, 1, 1) and
        expression(1, 0, 0) and expression(1, 1, 0) and
        expression(1, 0, 1) and expression(1, 1, 1)):
    print('This statement is true')
else:
    print('This statement is false')
