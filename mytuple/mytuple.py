# 元组创建后，就不能改变

t = (1,2,3,4,5)
# 5
print(len(t))

t= t + (6,7)
print(t)

# 1
print(t[0])

# 第3个位置
print(t.index(4))

# 4的出现次数
print(t.count(4))

 # 报错  不可变
# t[2]=10

