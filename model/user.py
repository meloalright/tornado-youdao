from lib.query import Query
from lib.security import gen_hash, check

class UserModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "user"
        super(UserModel, self).__init__()
        self.db = db


    def sign_up_object(self, name, email, password):
        hash_password = gen_hash(password)
        self.add('(NAME, EMAIL, PASSWORD) VALUES ("{name}", "{email}", "{password}")'.format(name=name, email=email, password=hash_password))

    def update_password(self, id, password):
        hash_password = gen_hash(password)
        self.update('SET PASSWORD = "{password}" WHERE ID = {id}'.format(password=hash_password, id=id))

    def valid_user(self, name, password):
        cur = self.select_one('WHERE NAME = "{name}"'.format(name=name))
        if cur:
            hash_password = cur[3]

            if check(password, hash_password):
                return {
                    'id': cur[0],
                    'name': cur[1],
                    'email': cur[2]
                }
            else:
                return None
        else:
            return None

    def get_user_note_list(self, id):
        cur = self.execute('SELECT T2.ID, T2.NAME, T2.ISCOMMON FROM {table} AS T1 JOIN NOTE AS T2 ON T1.ID = T2.AUTHOR WHERE T2.AUTHOR = {id}'.format(table=self.table_name, id=id))
        olist = [{'id': o[0], 'name': o[1], 'iscommon': o[2]} for o in cur]
        return olist
