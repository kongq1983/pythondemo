import decimal

d = decimal.Decimal('3.141')
print(d+1)

print(decimal.Decimal('1.00')/decimal.Decimal('3.00'))

decimal.getcontext().prec=3
print(decimal.Decimal('3.141')/decimal.Decimal('1.00'))
print(decimal.Decimal('1')/decimal.Decimal('6'))
print(decimal.Decimal('1.00')/decimal.Decimal('3.00'))