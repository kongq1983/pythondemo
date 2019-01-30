import  random


# randint


for i in range(5, 10):
    #整数
    print(random.randint(i,100))
    #浮点数
    print(random.uniform(i,100))
    print("-----------------------")

# x in the interval [0, 1).
print(random.random())