n = int(input('n: '))
a = list(map(int, input('Введіть числа 1-го масиву : ').split(' ')))

if len(a) != n:
    raise Exception("Хибне значення n")

m = int(input('m: '))
b = list(map(int, input('Введіть числа 2-го масиву : ').split(' ')))
if len(b) != m:
    raise Exception("Хибне значення m")

result = []
for el in a:
    if el not in b:
        result.append(el)

print(len(result))
print(*result)