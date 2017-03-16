import os
from lib.diff import differ
from lib.diff import merger

dirs = './diff-note/'

source = open(dirs + 'source.txt', 'r').read()
dist = open(dirs + 'dist.txt', 'r').read()
dist_branch = open(dirs + 'dist_branch.txt', 'r').read()

def test_diff():
    global source
    global dist

    d = differ()
    '''
    打印diff_patch
    '''
    print('======diff-lazy-patch======')
    for line in d.diff(source, dist):
        print('@{pos} {type} {str}'.format(pos=line['pos'], type=line['type'], str=line['str']))

    '''
    打印diff逻辑矩阵
    '''
    print('======lazy-matrix======')
    for line in d.diff(source, dist):
        print(line)

def test_merge():
    global source
    global dist
    global dist_branch
    m = merger()
    '''
    测试merge逻辑
    '''
    print('======merge======')
    dist = m.merge(source, dist, dist_branch)
    print(dist)


if __name__ == '__main__':
    test_diff()
    test_merge()
