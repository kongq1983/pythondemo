
list = [1,2,3]

#尾部添加1个元素
#[1, 2, 3, 4]
list.append(4)
print(list)

#尾部添加1个元素
#[1, 2, 3, 4, 5]
list[len(list):] = [5]
print(list)

list1 = [6,7,8]

# a[len(a):] = iterable

#[1, 2, 3, 4, 5, 6, 7, 8]
list.extend(list1)

print(list)

list2 = [9,10]
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list[len(list):] = list2
print(list)

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.insert(0,0)
print(list)

#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.remove(0)
print(list)
#10
print(list.pop())
#1
print(list.pop(0))

print(list.index(5))
#找不到会报错
#print(list.index(5,4,5))


print(list.count(5))

#[9, 8, 7, 6, 5, 4, 3, 2]
list.reverse()

print(list)

#[9, 8, 7, 6, 5, 4, 3, 2]
copyList = list.copy()
print(copyList)