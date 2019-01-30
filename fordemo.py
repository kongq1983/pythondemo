
# import math

# 0-4
for i in range(5):
    print(i)

# 5-9
for i in range(5, 10):
    print(i)


vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([abs(x) for x in vec])


freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])


print([(x, x**2) for x in range(6)])


# print([str(round(pi, i)) for i in range(1, 6)])



matrix  = [
    [1, 2, 3, 4,0],
    [5, 6, 7, 8,0],
    [9, 10, 11, 12,0],
]


print(list(zip(*matrix)))
