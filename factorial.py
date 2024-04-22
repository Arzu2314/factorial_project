def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    num = int(input("Введите число: "))
    print("Факториал числа", num, "равен", factorial(num))
    
    