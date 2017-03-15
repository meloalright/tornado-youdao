from lib.query import Query

class UserModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "user"
        super(UserModel, self).__init__()


    def sign_up_object(self):
        pass

