

list = [123,'spam',1.23]

print(list)

for x in list :
    print(x)


#123
print(list[0])

# [123,'spam']
print(list[:-1])

# [123, 'spam', 1.23, 4, 5, 6]
list = list + [4,5,6]
print(list)
[123, 'spam', 1.23, 4, 5, 6, 7]
list.append(7)
print(list)

# 1.23
print(list.pop(2))
# [123, 'spam', 4, 5, 6, 7]
print(list)

# print(list.sort())
print(list)

list1 = [8,3,1,6,10]

# [1, 3, 6, 8, 10]
list1.sort()
print(list1)

# [10, 8, 6, 3, 1]
list1.reverse()
print(list1)

for x in list1:
    print(x)