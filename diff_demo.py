import os
from lib.diff import differ


dirs = './diff-note/'

source = open(dirs + 'source.txt', 'r').read()
dist = open(dirs + 'dist.txt', 'r').read()

d = differ()

print('======source======')
print(source)
print('======dist======')
print(dist)
print('======diff======')
for line in d.diff(source, dist):
    print('@{pos} {str}'.format(pos=line['pos'], str=line['str']))

print('======matrix======')
for line in d._create_diff_matrix(source, dist):
    print(line)




'''
>> python3 diff_demo.py 
======source======
七步诗

煮豆燃豆萁
豆在釜中泣
本是同根生
相煎何太急

曹植
======dist======
完整版
七步诗

煮豆持作羹
漉菽以为汁
萁在釜下燃
豆在釜中泣
本自同根生
相煎何太急

曹植
======diff======
@0 + 完整版
@3 - 煮豆燃豆萁
@3 + 煮豆持作羹
@4 + 漉菽以为汁
@5 + 萁在釜下燃
@7 - 本是同根生
@7 + 本自同根生
======matrix======
[None, None, None, None, None, None, None, None]
[1, None, None, None, None, None, None, None]
[None, 2, None, None, None, None, None, None]
[None, None, None, None, None, None, None, None]
[None, None, None, None, None, None, None, None]
[None, None, None, None, None, None, None, None]
[None, None, None, 6, None, None, None, None]
[None, None, None, None, None, None, None, None]
[None, None, None, None, None, 8, None, None]
[None, None, None, None, None, None, 9, None]
[None, None, None, None, None, None, None, 10]
'''