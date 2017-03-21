from lib.query import Query

class NoteModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "note"
        super(NoteModel, self).__init__()
        self.db = db

    def create_note_object(self, name, author, iscommon, sub):
        self.add('(NAME, AUTHOR, ISCOMMON, SUB) VALUES ("{name}", "{author}",\
            "{iscommon}", "{sub}")'.format(name=name, author=author, iscommon=iscommon, sub=sub))

    def set_common(self, id):
        self.update('SET ISCOMMON = 1 WHERE ID = {id}'.format(id=id))

    def set_uncommon(self, id):
        self.update('SET ISCOMMON = 0 WHERE ID = {id}'.format(id=id))

    def update_note(self, id, name, sub):
        self.update('SET NAME = "{name}" , SUB = "{sub}" WHERE ID = {id}'.format(name=name, sub=sub, id=id))

    def delete_note(self, id):
        self.delete('WHERE ID = {id}'.format(id=id))

    def get_note(self, id):
        cur = self.select_one('WHERE ID = {id}'.format(id=id))
        if cur:
            return {
                'id': cur[0],
                'name': cur[1],
                'author': cur[2],
                'iscommon': cur[3],
                'sub': cur[4],
            }
        else:
            return None