# 2. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

expression = 1

for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} '
                  f'will be {(not (x or y or z)) == (not x and not y and not z)}')
            expression = expression and (not (x or y or z)) == (not x and not y and not z)

print(f'This statement {expression}')