

line = 'aaa,bbb,ccc,ddd,dd'

array = line.split(',')

for x in array :
    print(x)


line = '  aa,bb,cccc,dd  '
print(line)
#右边去掉空格
print(line.rstrip())
#左边去掉空格
print(line.lstrip())

# 两边去掉空格
print(line.strip())

