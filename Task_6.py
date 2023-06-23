'''Напишите программу банкомат.
- Начальная сумма равна нулю
- Допустимые действия: пополнить, снять, выйти
- Сумма пополнения и снятия кратны 50 у.е.
- Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
- После каждой третей операции пополнения или снятия начисляются проценты - 3 %
- Нельзя снять больше, чем на счёте
- При превышении суммы в 5 млн, вычитать налог на богатство 10 % перед каждой операцией, даже ошибочной
- Любое действие выводит сумму денег'''

import sys

class card:
    BALANCE = 0
    MIN = 50
    MAX = 5_000_000
    RATE = 0.015
    BONUSRATE = 0.03
    COUNT = 0
    TAX = 0.1

def add_money():
    money = int(input('Введите сумму пополнения, кратную 50 у.е.: '))
    if money % 50 == 0:
        card.BALANCE += money
        print(f'Вы пополнили счет на {money} у.е. ')
        card.COUNT += 1.
    else:
        print('Сумма пополнения не кратна 50 у.е.')

def get_money() -> int:
    money = int(input('Введите сумму снятия, кратную 50 у.е.: '))
    if money > card.BALANCE:
        print('Запрашиваемая сумма, больше чем сумма на счете.')
    elif money % 50 == 0:
        if money * card.RATE < 30:
            rate = 30
        elif money * card.RATE > 600:
            rate = 600
        else:
            rate = money * card.RATE
        card.BALANCE = card.BALANCE - money - rate
        print(f'Вы сняли со счета {money} и проценты за снятие {rate} у.е.')
        card.COUNT += 1
    else:
        print('Сумма снятия не кратна 50 у.е.')

def add_bonus():
    BONUSSUM = card.BALANCE * card.BONUSRATE
    card.BALANCE += card.BALANCE * card.BONUSRATE
    print(f'Начислен бонус: {BONUSSUM}')

while True:
    print(f'Cумма на счету составляет {card.BALANCE} у.е.')
    print('Выберите действие:\n\
    1 - Пополнить\n\
    2 - Снять\n\
    3 - Выйти')
    choise = input("Введите цифру: ")
    if card.BALANCE > card.MAX:
        TAX = card.BALANCE * card.TAX
        card.BALANCE -= TAX
        print(f'С вас списали налог на богатство в размере {TAX}')

    elif int(choise) == 1:
        #case '1':
            add_money()
            
    elif int(choise) == 2:
            get_money()
            
    elif int(choise) == 3:
            sys.exit()

    if card.COUNT % 3 == 0:
        add_bonus()
    else:
        pass