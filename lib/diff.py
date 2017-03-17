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
        self._diff_list = []
        self._diff_matrix = []


    def _reset(self):
        self._diff_list = []
        self._diff_matrix = []


    #
    # 生成一个n*n的矩阵
    #
    def _create_matrix(self, source, dist):
        ls = source.split('\n')
        ld = dist.split('\n')
        mat = [[None for i in ls] for i in ld]
        return mat

    #生成一个转置
    def _trans(self, mat):
        new_mat = []
        for i in range(0, len(mat[0])):
            new_line = [line[i] for line in mat]
            new_mat.append(new_line)
        return new_mat



    # 初始化diff逻辑字符串列表
    # NOT BLACK BOX
    def _init_diff_list(self, source, dist):
        ls = source.split('\n')
        ld = dist.split('\n')
        size = max(len(ls), len(ld))
        self._diff_list = [[] for i in range(0, size)]


    # 初始化diff矩阵
    # NOT BLACK BOX
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
    # p           - - 7
    #             - -
    #             -5c
    #               -6o
    # (dist)
    # ====================
    def _init_diff_matrix_lazy(self, source, dist):
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
        self._diff_matrix = mat





    #
    #
    # @ lazy
    #
    # lazy压入[+]逻辑
    def _push_plus_diff_lazy(self, source, dist):
        diff_mat = self._diff_matrix

        f = 0

        #answer = []

        for ils in range(0, len(diff_mat)):
            line = diff_mat[ils]
            sets = set(line)
            if sets == {None}:
                self._diff_list[f].append({'pos': f, 'type': '+', 'str': '%s'%dist.split('\n')[ils]})
                #f = f + 1
            else:
                sets.remove(None)
                f = list(sets)[0] + 1

    #
    #
    # @ lazy
    #
    # 压入[-]逻辑
    def _push_minus_diff_lazy(self, source, dist):
        trans_mat = self._trans(self._diff_matrix)

        f = 0

        answer = []

        for ils in range(0, len(trans_mat)):
            line = trans_mat[ils]
            sets = set(line)
            if sets == {None}:
                self._diff_list[f].append({'pos': f, 'type': '-', 'str': '%s'%source.split('\n')[ils]})
                f = f + 1
                ####
            else:
                sets.remove(None)
                f = list(sets)[0] + 1



    #
    #
    # @ lazy
    #
    # lazydiff调用入口
    def diff(self, source, dist):
        self._init_diff_list(source, dist)
        self._init_diff_matrix_lazy(source, dist)
        self._push_minus_diff_lazy(source, dist)
        self._push_plus_diff_lazy(source, dist)

        answer = []
        for l in self._diff_list:
            answer += l
        self._reset()
        return answer





class merger(object):

    def __init__(self):
        self.mergeList = []


    def _match_diff_truth(self, patch_line):
        truth = {'+':0, '-':0}
        for o in patch_line:
            if o['type'] == '+':
                truth['+'] += 1
            elif o['type'] == '-':
                truth['-'] += 1
        return truth

    def _append(self, source_line, plus_line):
        dist_line = []
        for o in plus_line:
            dist_line.append(o['str'])
        dist_line.append(source_line)
        return dist_line


    def _confict(self, source_line, patch_line):
        dist_line = []
        for o in patch_line:
            dist_line.append(o['type'] + o['str'])
        dist_line.append('source:' + source_line)
        return dist_line

    def _filt_plus_line(self, patch_line):
        return [o for o in patch_line if o['type'] == '+']
    
    # 真值匹配
    #(-)=0 (+)=more : append
    #(-)=1 (+)=more : empty+apppend
    #
    #(-)=2 (+)=0 : empty
    #(-)=2 (+)=more : confict
    def _truth_table_match(self, source_line, patch_line):
 
        dist = ''
        dist_line = []
        truth = self._match_diff_truth(patch_line)

        #print('truth')
        #print(patch_line)
        #print(truth)
        #print('truth')

        if truth['-'] == 0 and truth['+'] > 0:
            #(-)=0 (+)=more : append
            plus_line = patch_line
            dist = self._append(source_line, plus_line)
        elif truth['-'] == 1 and truth['+'] > 0:
            #(-)=1 (+)=more : empty+apppend
            plus_line = self._filt_plus_line(patch_line)
            dist = self._append('', plus_line)
        elif truth['-'] == 2 and truth['+'] == 0:
            #(-)=2 (+)=0 : empty
            dist = []
        elif truth['-'] == 2 and truth['+'] > 0:
            #(-)=2 (+)=more : confict
            dist = self._confict(source_line, patch_line)

        return dist


    #
    #
    # @ merge
    # @ 将两个diff_patch合并
    #
    #[{'str': '+ 完整版', 'pos': 0},
    # {'str': '- 煮豆燃豆萁', 'pos': 2},
    # {'str': '+ 煮豆持作羹', 'pos': 2},
    # {'str': '+ 漉菽以为汁', 'pos': 2},
    # {'str': '+ 萁在釜下燃', 'pos': 2}, \
    # {'str': '- 本是同根生', 'pos': 4},
    # {'str': '+ 本自同根生', 'pos': 4}]
    #
    #
    # [{'pos': 5, 'str': '相煎何太急', 'type': '-'}
    # {'pos': 5, 'str': '相煎何太急?!', 'type': '+'}
    # {'pos': 7, 'str': '曹植', 'type': '-'}
    # {'pos': 7, 'str': '曹植作', 'type': '+'}]
    #
    #
    def merge(self, source, dist_1, dist_2):
        #生成2个difflist
        d1 = differ()
        d1._init_diff_list(source, dist_1)
        d1._init_diff_matrix_lazy(source, dist_1)
        d1._push_minus_diff_lazy(source, dist_1)
        d1._push_plus_diff_lazy(source, dist_1)
        #
        d2 = differ()
        d2._init_diff_list(source, dist_2)
        d2._init_diff_matrix_lazy(source, dist_2)
        d2._push_minus_diff_lazy(source, dist_2)
        d2._push_plus_diff_lazy(source, dist_2)
        print(d1._diff_list)
        print(d2._diff_list)
        #
        # 创建mergeList
        #
        source_read = source.split('\n')
        mergeList = [[] for i in range(0, max(len(d1._diff_list), len(d2._diff_list)))]
        #
        # merge patch here
        #
        for i in range(0, len(mergeList)):
            ''''''
            try:
                diff_line = d1._diff_list[i]
                for o in diff_line:
                    mergeList[i].append(o)
            except:
                pass
            ''''''
            try:
                diff_line = d2._diff_list[i]
                for o in diff_line:
                    mergeList[i].append(o)
            except:
                pass

        merge_dist_list = [self._truth_table_match(source_read[index], mergeList[index]) for index in range(0, len(source_read))]
        print(merge_dist_list)
        dist = ''
        for str_line in merge_dist_list:
            if str_line == '':
                dist += '\n\n'
            else:
                try:
                    dist += ('\n').join(str_line)
                except:
                    pass
        return dist
