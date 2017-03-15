#
# diff.py
#
# 用于对比两段文本的区别
#
# author: melowhtang
#
# github: meloalright
#
#

class differ(object):

    def __init__(self):
        self.switch = True

    #
    # 生成一个n*n的矩阵
    #
    def _create_matrix(self, source, dist):
        ls = source.split('\n')
        ld = dist.split('\n')
        mat = [[None for i in ls] for i in ld]
        return mat

    #
    # diff 矩阵
    # ===================
    #   a a a c a c o p(source)
    # a 1         - -
    # a   2       - -
    # a     3     - -
    # k ++++++++++x+x+++++++4k
    # c       5   - -
    # a         6 - -
    # b ++++++++++x+x+++++++7b
    # p           - - 9
    #             -7c
    #               -8o

    # (dist)
    # ====================
    def _create_diff_matrix(self, source, dist):
        mat = self._create_matrix(source, dist)

        f = 0

        source_readlist = source.split('\n')
        dist_readlist = dist.split('\n')

        for its in range(0, len(source_readlist)):
            for ids in range(f, len(dist_readlist)):
                si = source_readlist[its]
                di = dist_readlist[ids]

                if si == di:
                    mat[ids][its] = f
                    f = f + 1
                    break
                else:
                    f = f + 1
                    pass

        if self.switch:
            self.switch = False
            print('''mat =''')
            for line in mat:
                print('{line}\n'.format(line=line))
        return mat

    def trans(self, mat):
        new_mat = []
        for i in range(0, len(mat[0])):
            new_line = [line[i] for line in mat]
            new_mat.append(new_line)
        return new_mat


    # 获取+逻辑
    def _fetch_plus_diff(self, source, dist):
        diff_mat = self._create_diff_matrix(source, dist)

        f = 0

        answer = []

        for ils in range(0, len(diff_mat)):
            line = diff_mat[ils]
            if set(line) == {None}:
                answer.append({f: '+ %s'%dist.split('\n')[ils]})
                f = f + 1
            else:
                f = f + 1

        return answer

    # 获取-逻辑
    def _fetch_minus_diff(self, source, dist):
        trans_mat = self.trans(self._create_diff_matrix(source, dist))

        f = 0

        answer = []

        for ils in range(0, len(trans_mat)):
            line = trans_mat[ils]
            sets = set(line)
            if sets == {None}:
                answer.append({f: '- %s'%source.split('\n')[ils]})
                f = f + 1
            else:
                sets.remove(None)
                f = list(sets)[0] + 1
        return answer

    def diff(self, source, dist):
        return self._fetch_plus_diff(source, dist) + self._fetch_minus_diff(source, dist)

df = differ()
diff = df.diff('today is so well\nyou know\nright\n2017\nend',
               'today is so well\nyeah\nwakawaka\nyou know\nright\n2017.3.16')


print(diff)
