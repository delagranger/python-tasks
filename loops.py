def loops_task33():
    """
    Дано натуральное число. 
    Напишите программу, которая определяет, является ли последовательность его цифр 
    при просмотре справа налево упорядоченной по неубыванию.
    """

    n = int(input()) 
    flag = True
    last_dig = n % 10
    n //= 10

    while n != 0:
        curr_dig = n % 10

        if curr_dig < last_dig:
            flag = False
            break
        
        last_dig = curr_dig
        n //= 10
    
    print("YES" if flag else "NO")





    








            
