#!/usr/bin/env python3

# -*-coding:utf-8 -*-


amount = int(input("Enter amount: "))


if amount <= 0:
    print('Valor tem que ser maior que zero')
    discount =0
elif amount <= 1000:
    discount = amount * 0.05
    print('Discount', discount)
elif amount <= 5000:
    discount = amount * 0.10
    print('Discount', discount)
elif amount <= 8000:
    discount = amount * 0.15
    print('Discount', discount)
else:
    discount = amount * 0.20
    print('Discount', discount)

print('Pagamento via internet com desconto: ', amount - discount)
print('Obrigado pela sua compra volte sempre.')