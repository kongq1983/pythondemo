

dict = {'food':'Spam','quantity':4,'color':'pink'}

#pink
print(dict['color'])

# {'food': 'Spam', 'quantity': 5, 'color': 'pink'}
dict['quantity']+=1
print(dict)

dict = {}
dict['id']=1
dict['nage']='king'
dict['job']='it'

print(dict)

# keys
keys = list(dict.keys())
for key in keys :
    print(key)


# 打印key and value
for key in keys :
    print(key,'=>' ,dict[key])


# 根据key排序
dict = {'a': 5,'b':1,'c': 6}

for key in sorted(dict) :
    print(key,'=>',dict[key])


for c in 'spam':
    print(c.upper())

# [1, 4, 9, 16, 25]
squares = [x ** 2 for x in [1,2,3,4,5]]
print(squares)

dict['e']=10
# 会报错 dict['f']
# dict['f']

# False
print('f' in dict)


if not 'f' in dict :
    print('f',' not exists')

# 0
value = dict.get('f',0)
print(value)

value = dict['f'] if 'x' in dict else 0