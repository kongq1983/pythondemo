



basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
#{'banana', 'apple', 'pear', 'orange'}
print(basket)
#true
print( 'orange' in basket)
#false
print( 'orange1' in basket)

a = set('abracadabra')
#{'a', 'c', 'd', 'b', 'r'}
print(a)


a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

