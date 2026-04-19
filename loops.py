def Loops_Task29():
# Дано натуральное число. 
# Напишите программу, которая меняет порядок цифр числа на обратный.

    n = int(input())
    n_new = ""

    while n != 0:
        last_digit = str(n % 10)
        n_new += last_digit
        n //= 10
    
    print(n_new)







            
