import os
from lib.diff import differ
from lib.diff import merger

dirs = './diff-note/'

source = open(dirs + 'source.txt', 'r').readlines()
dist = open(dirs + 'dist.txt', 'r').readlines()
dist_branch = open(dirs + 'dist_branch.txt', 'r').readlines()

def test_diff():
    d = differ()
    '''
    打印diff_patch
    '''
    hightlight = d.highlight_diff(source, dist)
    print(hightlight)


def test_merge():
    m = merger()
    '''
    测试merge逻辑
    '''
    this_dist = m.merge(source, dist, dist_branch)
    print('======merge======')
    print(this_dist)


if __name__ == '__main__':
    test_diff()
    test_merge()
