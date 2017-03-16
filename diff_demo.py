import os
from lib.diff import differ

def test():
    dirs = './diff-note/'

    source = open(dirs + 'source.txt', 'r').read()
    dist = open(dirs + 'dist.txt', 'r').read()

    d = differ()

    print('======source======')
    print(source)

    print('======dist======')
    print(dist)


    print('======diff-lazy-patch======')
    for line in d.diff_lazy_patch(source, dist):
        print('@{pos} {str}'.format(pos=line['pos'], str=line['str']))


    print('======lazy-matrix======')
    for line in d._create_diff_matrix_lazy(source, dist):
        print(line)


if __name__ == '__main__':
    test()
