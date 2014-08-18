s = file('source.txt', 'r').read()
dic = {}
for ch in s:
    if ch in dic:
        dic[ch] += 1
    else :
        dic[ch] = 1
res = ''
for i in dic:
    if dic[i] == 1:
        res += i
p = ''
for ch in s:
    if ch in res:
        p += ch
print p
