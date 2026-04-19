def Loops_Task30():
# Дано натуральное число. Напишите программу, которая вычисляет:
#
# - сумму его цифр;
# - количество цифр в нем;
# - произведение его цифр;
# - среднее арифметическое его цифр;
# - его первую цифру;
# - сумму его первой и последней цифры.
    
    n = int(input())
    dig_sum = 0
    dig_count = 0
    dig_prod = 1
    last_dig = n % 10
    first_dig = 0
    

    while n != 0:
        curr_digit = n % 10

        dig_sum += curr_digit
        dig_count += 1
        dig_prod *= curr_digit
        if curr_digit < 10:
            first_dig = curr_digit

        n //= 10

    digs_arth_mean = dig_sum / dig_count
    first_and_last_dig_sum = last_dig + first_dig

    print(dig_sum, dig_count, dig_prod, digs_arth_mean, first_dig, first_and_last_dig_sum, sep='\n')
    








            
