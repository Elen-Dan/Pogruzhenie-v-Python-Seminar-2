'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.'''

import fractions

numerator_1, denominator_1 = map(int, input('Введите числитель и знаменатель первой дроби, пример A/B: ').split("/"))
numerator_2, denominator_2 = map(int, input('Введите числитель и знаменатель второй дроби, пример C/D: ').split("/"))

d1 = numerator_1 * numerator_2
d2 = denominator_1 * denominator_2
g1 = numerator_1 * denominator_2 + numerator_2 * denominator_1
g2 = denominator_1 * denominator_2

def gcd_loop(a, b):
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if(a % i == 0) and (b % i == 0):
            gcd = i
    return gcd


gcd_mult = gcd_loop(d1, d2)
gcd_sum = gcd_loop(g1, g2)

print(f'Произведение дробей: {int(d1/gcd_mult)}/{int(d2/gcd_mult)}')
print(f'Сумма дробей: {int(g1/gcd_sum)}/{int(g2/gcd_sum)}')

f1 = fractions.Fraction(numerator_1, denominator_1)
f2 = fractions.Fraction(numerator_2, denominator_2)
print(f"Проверка умножения через fractions: {f1 * f2}")
print(f"Проверка сложения через fractions: {f1 + f2}")