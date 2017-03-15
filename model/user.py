from lib.query import Query

class UserModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "user"
        super(UserModel, self).__init__()

    def test_conn(self):
        db = self.db
        db.execute("DROP TABLE IF EXISTS USER");
        db.execute('''CREATE TABLE USER
                   (ID INT PRIMARY KEY     NOT NULL,
                    NAME           TEXT    NOT NULL,
                    SUB        CHAR(50));
                   ''')

        self.add(1, 'youdao' ,'test')
        self.add(2, 'youdao' ,'tornado')
        self.add(3, 'youdao' ,'netease')
        self.update('set sub = 163 where id = 2')
        self.delete('where id = 3')
        print(self.select('where id >= 1'))
        db.execute("DROP TABLE IF EXISTS USER");

