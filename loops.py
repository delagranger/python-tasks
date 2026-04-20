def Loops_Task31():
# Дано натуральное число n (n > 9). 
# Напишите программу, которая определяет его вторую (с начала) цифру.

    n = int(input())

    while len(str(n)) >= 2:
        last_digit = n % 10
        n //= 10
    
    print(last_digit)
    








            
