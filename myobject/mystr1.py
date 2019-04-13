import re
# all
s1 = '%s,eggs,and %s' % ('spam','Spam')

# 2.6  3.0
s2 = '{0},eggs,and {1}'.format('spam','Spam')

print(s1)
print(s2)

msg = """
    welcome
        to 
            you
                !

"""

print(msg)

msg = '''
    1
    2
    3
'''
print(msg)


#正则
# Python
match = re.match('Hello[ \t]*(.*)world','Hello Python world')
print(match.group(1))