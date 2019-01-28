

import urllib, sys
from contextlib import closing
#
# # with closing(urllib.urlopen('http://www.baidu.com')) as f:
# #     for line in f:
# #         sys.stdout.write(line)
#
# with closing(urllib.urlopen('https://www.baidu.com')) as f:
#     for line in f:
#         sys.stdout.write(line)


import urllib.request

def run_demo():
    f = urllib.request.urlopen('http://www.baidu.com')
    print(f.read())
    print(2 ** 7)

if __name__=='__main__':
    run_demo()
















