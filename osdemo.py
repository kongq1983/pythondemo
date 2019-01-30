# os api operate

import  os

#nt
print(os.name)

#<module 'ntpath' from 'C:\\develop\\python37\\lib\\ntpath.py'>
print(os.path)

# .
print(os.curdir)
#..
print(os.pardir)

#\
print(os.sep)

#.
print(os.extsep)

#/
print(os.altsep)

print(os.pathsep)
#;
print(os.linesep)
#.;C:\bin
print(os.defpath)
#nul
print(os.devnull)

# cpu count
print(os.cpu_count())


# - all functions from posix or nt, e.g. unlink, stat, etc.
# - os.path is either posixpath or ntpath
# - os.name is either 'posix' or 'nt'
# - os.curdir is a string representing the current directory (always '.')
# - os.pardir is a string representing the parent directory (always '..')
# - os.sep is the (or a most common) pathname separator ('/' or '\\')
# - os.extsep is the extension separator (always '.')
# - os.altsep is the alternate pathname separator (None or '/')
# - os.pathsep is the component separator used in $PATH etc
# - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
# - os.defpath is the default search path for executables
# - os.devnull is the file path of the null device ('/dev/null', etc.)

