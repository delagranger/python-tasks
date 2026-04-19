def Loops_Task27():
# На вход программе подаются четыре целых числа, 
# которые задают временной промежуток от h₁:m₁ до h₂:m₂. 
# Напишите программу, которая выводит все моменты времени между этими промежутками 
# (включая границы) в формате hh:mm с интервалом в 1 минуту, каждый на отдельной строке.

    first_range = int(input()) * 60 + int(input())
    second_range = int(input()) * 60 + int(input())

    while first_range <= second_range:
        h = first_range // 60
        if h < 10:
            h = '0' + str(h)
        m = first_range - first_range // 60 * 60
        if m < 10:
            m = '0' + str(m)

        print(f"{h}:{m}")

        first_range += 1




            
