def strings_task3():
    """
    На вход программе подаётся одна строка. 
    Напишите программу, которая выводит в столбик элементы строки в обратном порядке.
    """

    s = input()

    for i in range(len(s) - 1, -1, -1):
        print(s[i])


def strings_task4():
    """
    На вход программе подаются три строки: имя, фамилия и отчество 
    (именно в таком порядке). 
    Напишите программу, которая выводит инициалы человека.
    """

    name, surname, patron = input(), input(), input()

    print(surname[0], name[0], patron[0], sep='')


def strings_task5():
    """
    На вход программе подаётся строка из эмодзи-символов – очередь животных на борт самолёта. 
    Для каждого животного из очереди вам необходимо вывести его эмодзи и номер в очереди (начиная с 1)
    """

    animals = input()

    for i in range(len(animals)):
        print(f"{i + 1}) {animals[i]}")


def strings_task6():
    """
    На вход программе подаётся одна строка состоящая из цифр. 
    Напишите программу, которая считает сумму цифр данной строки.
    """

    nums = input()
    sum = 0

    for i in nums:
        sum += int(i)
    
    print(sum)


def strings_task7():
    """
    На вход программе подаётся одна строка. 
    Напишите программу, которая выводит сообщение «Цифра» (без кавычек), 
    если строка содержит цифру. В противном случае вывести сообщение «Цифр нет» (без кавычек).
    """

    string = input()
    is_num = False

    for i in string:
        try:
            int(i)
            is_num = True
            break
        except ValueError:
            continue

    print("Цифра" if is_num else "Цифр нет")


def strings_task8():
    """
    На вход программе подаётся одна строка. 
    Напишите программу, которая определяет, сколько раз в строке встречаются символы + и *
    """

    string = input()
    count_plus = 0
    count_prod = 0

    for i in string:
        if i == '+':
            count_plus += 1
        elif i == '*':
            count_prod += 1
    
    print(f"Символ + встречается {count_plus} раз")
    print(f"Символ * встречается {count_prod} раз")


def strings_task9():
    """
    На вход программе подаётся одна строка. 
    Напишите программу, которая определяет, сколько в ней пар одинаковых соседних символов.
    """

    string = input()
    counter = 0

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            counter += 1
        
    print(counter)
