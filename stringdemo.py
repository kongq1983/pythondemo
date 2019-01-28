import math

str = 'welcome to python';


print(str.count("o"))
print(str.split(" "))
print( str[3:])

print(str)



the_world_is_flat = True

if the_world_is_flat:
   print("Be careful not to fall off!")


#C:\some
#ame
print('C:\some\name')

#C:\some\name
print(r'C:\some\name')

print("C:\some\name")


str = "a1234567890"
print(len(str))


print(math.ceil(-5))

print(math.fabs(-5))

print(math.floor(-5))

def myrepeat(self):
    self = '*' +self +'*'
    return self;



print(myrepeat('8'))

#00042
print("42".zfill(5))

#-0042
print("-42".zfill(5))


#fbcfbcfbc
a = "abcabcabc"
print(a.replace("a", "f"))


a = b"abc"
b = a.replace(b"a", b"f")
#b'fbc'
print(b)

a = b"abcbabc"
b = a.replace(b"a", b"f")
#b'fbcbfbc'
print(b)

#ABCDEF
print('abcdEf'.upper())
#True
print('ABC'.isupper())

#true
print(b'Py' in b'Python')

#3
print("abcdef".find("d"))
# -1
print("abcdef".find("g"))

#3
print("abcdef".index("d"))
# 会报错
print("abcdef".index("g"))


a = [1,2,3,4,5]

print()
