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
        



    def valid_password(self, name, password):
        cur = self.select_one('WHERE NAME = "{name}"'.format(name=name))
        if cur:
            hash_password = cur[3]

            return check(password, hash_password)
        else:
            return False
