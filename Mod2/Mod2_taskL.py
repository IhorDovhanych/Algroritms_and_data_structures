n = int(input("Введіть кількість товару для 1-го магазину "))
a = list(map(int, input().split(sep=" ")))

if not len(a) == n:
    raise Exception("Хибна довжина цін товарів для 1-го магазину")
for i in range(n):
    if a[i] > 10**9:
        raise Exception("Ціни мають < 10^9")
    
m = int(input("Введіть кількість товару для 2го магазину "))
b = list(map(int, input().split(sep=" ")))

if not len(b) == m:
    raise Exception("Хибна довжина цін товарів для 1-го магазину")
for i in range(m):
    if b[i] > 10**9:
        raise Exception("Ціни мають < 10^9")

c = a + b
c = set(c)
print(sorted(list(c)))