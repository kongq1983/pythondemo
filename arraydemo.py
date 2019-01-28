

squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
#IndexError: list index out of range
#print(squares[8])

#[16, 25]
print(squares[3:])

squares1= squares + [36, 49, 64, 81, 100]
print(squares1)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 216]
squares1.append(216)
print(squares1)

#[1, 4, 'C', 'D', 'E', 36, 49, 64, 81, 100, 216]
squares1[2:5] = ['C', 'D', 'E']
print(squares1)
