
path = 'C:\\temp\\test.txt'

# 不追加
# f = open(path,'w')
# 追加
f = open(path,'a')
f.write("Hello\n")
f.write('world\n')

f.close()

f = open(path)
text = f.read()
print(text)

print(dir(f))