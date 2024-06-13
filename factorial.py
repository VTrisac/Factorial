def factorial(num=10):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1

print("El factorial de 5 es " + str(factorial(5)))
print("El factorial de 8 es " + str(factorial(8)))
print("El factorial del valor por defecto (10) es " + str(factorial()))
