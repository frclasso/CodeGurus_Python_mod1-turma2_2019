


amount = int(input("Enter amount: "))

if amount < 1000:
    discount = amount * 0.05
    print('Discount', discount)
else:
    discount = amount * 0.10
    print('Discount', discount)

print('Pagamento via internet com desconto: ', amount - discount)
print('Obrigado pela sua compra volte sempre.')