#
# diff.py
#
# 用于对比两段文本的区别
#
# author: melowhtang
#
# blog: meloalright.github.io
#
#

class differ(object):

    def __init__(self):
        self.switch = True
        self.diff_list = []

    # 初始化
    # diff逻辑字符串列表
    def _init_diff_list(self, source, dist):
        ls = source.split('\n')
        ld = dist.split('\n')
        size = len(ls) + len(ld)
        self.diff_list = [[] for i in range(0, size - 1)]

    #
    # 生成一个n*n的矩阵
    #
    def _create_matrix(self, source, dist):
        ls = source.split('\n')
        ld = dist.split('\n')
        mat = [[None for i in ls] for i in ld]
        return mat



    #
    # lazy_diff 矩阵
    # ===================
    #   a a a c a c o p(source)
    # a 0         - -
    # a   1       - -
    # a     2     - -
    # k ++++++++++x+x+++++++2k
    # c       3   - -
    # a         4 - -
    # b ++++++++++x+x+++++++4b
    # p           - - 8
    #             - -
    #             -4c
    #               -4o

    # (dist)
    # ====================

    def _create_diff_matrix_lazy(self, source, dist):
        mat = self._create_matrix(source, dist)

        f = 0
        memory = f

        source_readlist = source.split('\n')
        dist_readlist = dist.split('\n')



        for its in range(0, len(source_readlist)):
            for ids in range(f, len(dist_readlist)):
                si = source_readlist[its]
                di = dist_readlist[ids]

                if si == di:
                    mat[ids][its] = its
                    f = f + 1
                    #找到了就更新memory
                    memory = f
                    break
                else:
                    f = f + 1
                    pass
            #没找到就回退f=memory
            f = memory

        return mat

    #
    # diff 矩阵
    # ===================
    #   a a a c a c o p(source)
    # a 0         - -
    # a   1       - -
    # a     2     - -
    # k ++++++++++x+x+++++++3k
    # c       4   - -
    # a         5 - -
    # b ++++++++++x+x+++++++6b
    # p           - - 8
    #             - -
    #             -6c
    #               -7o
    # (dist)
    # ====================
    def _create_diff_matrix_active(self, source, dist):
        mat = self._create_matrix(source, dist)

        f = 0
        memory = f

        source_readlist = source.split('\n')
        dist_readlist = dist.split('\n')



        for its in range(0, len(source_readlist)):
            for ids in range(f, len(dist_readlist)):
                si = source_readlist[its]
                di = dist_readlist[ids]

                if si == di:
                    mat[ids][its] = f
                    f = f + 1
                    #找到了就更新memory
                    memory = f
                    break
                else:
                    f = f + 1
                    pass
            #没找到就回退f=memory
            f = memory

        return mat

    def _trans(self, mat):
        new_mat = []
        for i in range(0, len(mat[0])):
            new_line = [line[i] for line in mat]
            new_mat.append(new_line)
        return new_mat


    # 压入[+]逻辑
    def _push_plus_diff_active(self, source, dist):
        diff_mat = self._create_diff_matrix_active(source, dist)

        f = 0

        #answer = []

        for ils in range(0, len(diff_mat)):
            line = diff_mat[ils]
            if set(line) == {None}:
                self.diff_list[f].append({'pos': f, 'str': '+ %s'%dist.split('\n')[ils]})
                f = f + 1
            else:
                f = f + 1

        #return answer

    # 压入[-]逻辑
    def _push_minus_diff_active(self, source, dist):
        trans_mat = self._trans(self._create_diff_matrix_active(source, dist))

        f = 0

        answer = []

        for ils in range(0, len(trans_mat)):
            line = trans_mat[ils]
            sets = set(line)
            if sets == {None}:
                self.diff_list[f].append({'pos': f, 'str': '- %s'%source.split('\n')[ils]})
                f = f + 1
            else:
                sets.remove(None)
                f = list(sets)[0] + 1
        return answer


    #diff调用入口
    def diff_active_patch(self, source, dist):
        self._init_diff_list(source, dist)
        self._push_minus_diff_active(source, dist)
        self._push_plus_diff_active(source, dist)

        answer = []
        for l in self.diff_list:
            answer += l
        return answer


    #
    #
    # @ lazy
    #
    # lazy压入[+]逻辑
    def _push_plus_diff_lazy(self, source, dist):
        diff_mat = self._create_diff_matrix_lazy(source, dist)

        f = -1

        #answer = []

        for ils in range(0, len(diff_mat)):
            line = diff_mat[ils]
            sets = set(line)
            if sets == {None}:
                self.diff_list[f].append({'pos': f, 'str': '+ %s'%dist.split('\n')[ils]})
                #f = f + 1
            else:
                sets.remove(None)
                f = list(sets)[0]

        #return answer

    #
    #
    # @ lazy
    #
    # 压入[-]逻辑
    def _push_minus_diff_lazy(self, source, dist):
        trans_mat = self._trans(self._create_diff_matrix_lazy(source, dist))

        f = -1

        answer = []

        for ils in range(0, len(trans_mat)):
            line = trans_mat[ils]
            sets = set(line)
            if sets == {None}:
                self.diff_list[f].append({'pos': f, 'str': '- %s'%source.split('\n')[ils]})
                #f = f + 1
            else:
                sets.remove(None)
                f = list(sets)[0]
        return answer


    #
    #
    # @ lazy
    #
    # lazydiff调用入口
    def diff_lazy_patch(self, source, dist):
        self._init_diff_list(source, dist)
        self._push_minus_diff_lazy(source, dist)
        self._push_plus_diff_lazy(source, dist)

        answer = []
        for l in self.diff_list:
            answer += l
        return answer
