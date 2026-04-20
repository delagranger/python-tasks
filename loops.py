def loops_task34():
    """
    На вход программе подаётся натуральное число n. 
    Напишите программу, которая выводит для каждой четной цифры данного числа текст в следующем формате:
    <i>-я четная цифра равна <digit>
    """

    number = input()
    step = 1
    flag = False

    for digit in number:
        curr_dig = int(digit)

        if curr_dig % 2 == 0:
            print(f"{step}-я четная цифра равна {curr_dig}")
            step += 1
            flag = True
    
    if not flag:
        print("Четных цифр в числе нет")






    








            
