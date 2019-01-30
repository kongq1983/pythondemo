
tel = {'jack': 4098, 'sape': 4139}
print(tel['jack'])

del tel['sape']

print('jack' not in tel)

print(tel)


print({x: x**2 for x in (2, 4, 6)})


dd = dict(sape=4139, guido=4127, jack=4098)
print(dd)

print(dd['guido'])

# 0 tic
# 1 tac
# 2 toe
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)



