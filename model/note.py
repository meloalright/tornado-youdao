from lib.query import Query
from lib.cvt64 import *
from lib.diff import differ
import re

class NoteModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "note"
        super(NoteModel, self).__init__()
        self.db = db

    def create_note_object(self, name, author, iscommon, sub):
        self.add('(NAME, AUTHOR, ISCOMMON, SUB, HISTORY) VALUES ("{name}", "{author}",\
            "{iscommon}", "{sub}", "\n\n")'.format(name=name, author=author, iscommon=iscommon, sub=sub))

    def set_common(self, id):
        self.update('SET ISCOMMON = 1 WHERE ID = {id}'.format(id=id))

    def set_uncommon(self, id):
        self.update('SET ISCOMMON = 0 WHERE ID = {id}'.format(id=id))

    def update_note(self, id, name, sub):
        self.update('SET NAME = "{name}" , SUB = "{sub}" WHERE ID = {id}'.format(name=name, sub=sub, id=id))

    def push_history(self, id):
        #每次打开文件 先存一下历史
        self.update('SET HISTORY = SUB WHERE ID = {id}'.format(id=id))

    def delete_note(self, id):
        self.delete('WHERE ID = {id}'.format(id=id))

    def clear_hash(self, hash_id):
        return decvt64(hash_id)

    #### gen need ####
    def fetch_diff(self, id, callback):
        cur = self.select_one('WHERE ID = {id}'.format(id=id))
        if cur:
            r = re.compile(r'(.*\n)')
            sub = r.findall(cur[4])
            history = r.findall(cur[5])
            '''
            diff
            '''
            d = differ()

            hightlight = d.highlight_diff(history, sub)
            return callback(hightlight)
        else:
            return callback(None)

    def get_note(self, id, callback):
        cur = self.select_one('WHERE ID = {id}'.format(id=id))
        if cur:
            return callback({
                'name': cur[1],
                'author': cur[2],
                'iscommon': cur[3],
                'sub': cur[4],
                'history': cur[5],

            })
        else:
            return callback(None)