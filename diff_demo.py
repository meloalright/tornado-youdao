import os
from lib.diff import differ
from lib.diff import merger

dirs = './diff-note/'

source = open(dirs + 'source.txt', 'r').readlines()
dist = open(dirs + 'dist.txt', 'r').readlines()
dist_branch = open(dirs + 'dist_branch.txt', 'r').readlines()

def test_diff():
    global source
    global dist

    d = differ()
    '''
    打印diff_patch
    '''
    print('======diff-lazy-patch======')
    for line in d.diff(source, dist_branch):
        print('@{pos} {type} {str}'.format(pos=line['pos'], type=line['type'], str=line['str']))



def test_merge():
    global source
    global dist
    global dist_branch
    m = merger()
    '''
    测试merge逻辑
    '''
    dist = m.merge(source, dist, dist_branch)
    print('======merge======')
    print(dist)


if __name__ == '__main__':
    #test_diff()
    test_merge()
