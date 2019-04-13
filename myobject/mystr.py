
s = 'Spam'
# 长度 4
print(len(s))

#S
print(s[0])
#p
print(s[1])

#m
print(s[-1])

#a
print(s[-2])

#m
print(s[len(s)-1])

# pa
print(s[1:3])

# pam
print(s[1:])

# Spa
print(s[:3])

# Spam
print(s[:])

#Spam123
print(s+'123')

#SpamSpamSpamSpamSpamSpamSpamSpam
print(s*8)

# s[0]='a'   会报错

# 1
print(s.find('pa'))

# S--m
print(s.replace('pa','--'))

#SPAM
print(s.upper())

#True
print(s.isalpha())

# {'a', 'S', 'p', 'm'}
print(set(s))

for x in set(s):
    print(x)