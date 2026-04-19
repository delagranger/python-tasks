def Loops_Task29():
# Дано натуральное число n
# Напишите программу, которая определяет его максимальную и минимальную цифры

    n = int(input())
    max_dig = n % 10
    min_dig = n % 10

    while n != 0:
        last_dig = n % 10

        if last_dig > max_dig:
            max_dig = last_dig
        elif last_dig < min_dig:
            min_dig = last_dig
        
        n //= 10
    
    print(f"Максимальная цифра равна {max_dig}")
    print(f"Минимальная цифра равна {min_dig}")
        
        
    








            
