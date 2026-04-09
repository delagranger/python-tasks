# Формат входных данных
# На вход программе подаются два положительных действительных числа a и b​, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести 4 числа (каждое на отдельной строке) – среднее арифметическое, 
# геометрическое, гармоническое и квадратичное.

from math import sqrt, pow

a, b = float(input()), float(input())

arith_mean = (a + b) / 2
geom_mean = sqrt(a * b)
harm_mean = (2 * a * b) / (a + b)
sqr_mean = sqrt((pow(a, 2) + pow(b, 2)) / 2)

print(arith_mean, geom_mean, harm_mean, sqr_mean, sep="\n")