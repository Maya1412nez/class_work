s = open('24/14_14647.txt').readline()
import fnmatch

s = s.replace('X', 'X X').replace('Y', 'Y Y')
s = s.split()
m = 0
# X XlalalalY YX XlalalalX
# XSX XDDURSGVMREJMMEWUQOJHUJKWRFJCCBIWSY YTMY YROY YJNIX XIIKHAQXMXCINCWOSQWGAIYEUAGOUXVFCJNTNKHYVINRHOQQNRBJDQATAKBXPWEEVZDI
for i in range(1, len(s) - 1):
    if fnmatch.fnmatch((s[i - 1] + s[i] + s[i+1]), 'Y*YY*XX*X') or fnmatch.fnmatch((s[i - 1] + s[i] + s[i+1]), 'X*XX*YY*Y'):
        m = max(m , len(s[i - 1] + s[i] + s[i+1]))
        # print(s[i - 1] + s[i] + s[i+1])
print(m)