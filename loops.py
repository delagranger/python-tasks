def Loops_Task32():
# Дано натуральное число. 
# Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

    n = int(input())
    flag = True
    last_dig = n % 10
    n //= 10

    while n != 0:
        curr_dig = n % 10

        if curr_dig != last_dig:
            flag = False
            break

        last_dig = curr_dig
        n //= 10
    
    print("YES" if flag else "NO")


    








            
