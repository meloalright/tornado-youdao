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
======source======
七步诗

煮豆燃豆萁
豆在釜中泣
本是同根生
相煎何太急

曹植
======dist======
七步诗

煮豆持作羹
漉菽以为汁
萁在釜下燃
豆在釜中泣
本自同根生
相煎何太急

曹植
======diff======
@2 - 煮豆燃豆萁
@2 + 煮豆持作羹
@3 + 漉菽以为汁
@4 + 萁在釜下燃
@6 - 本是同根生
@6 + 本自同根生
======matrix======
[0, None, None, None, None, None, None, None]
[None, 1, None, None, None, None, None, None]
[None, None, None, None, None, None, None, None]
[None, None, None, None, None, None, None, None]
[None, None, None, None, None, None, None, None]
[None, None, None, 5, None, None, None, None]
[None, None, None, None, None, None, None, None]
[None, None, None, None, None, 7, None, None]
[None, None, None, None, None, None, 8, None]
[None, None, None, None, None, None, None, 9]
'''