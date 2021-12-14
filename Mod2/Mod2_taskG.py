n = int(input("Введіть кількість елементів масиву : "))
if not 0<n<=100:
    raise Exception("Хибне значення n")
result = ""
a = input()
nums = list(map(lambda el:int(el), a.split(sep=" ")))
if len(nums) == n:
    result+=str(nums[-1])+" "
    for i in range(len(nums)-1):
        result+=str(nums[i])+" "
else:
    print("Невірна кількість елементів")
print(result)