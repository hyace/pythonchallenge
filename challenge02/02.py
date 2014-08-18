'''
Created on 2014 8 17

@author: Chyace
'''
import string
s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. \
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgl\
e qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
res = ""
for ch in s:
    ch = ord(ch)
    if ch >= ord('a') and ch <= ord('z'):
        ch = (ch + 2 - ord('a')) % 26 + ord('a')
    res += chr(ch)
    
print res

# or
raw = 'abcdefghijklmnopqrstuvwxyz'
tran = 'cdefghijklmnopqrstuvwxyzab'
table = string.maketrans(raw, tran)
s = s.translate(table)
print s
print 'map'.translate(table)
