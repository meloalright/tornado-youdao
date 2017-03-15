#init_db.py
from lib.query import Query
import sqlite3

class initDbModel(Query):
    def __init__(self):
        super(initDbModel, self).__init__()
        self.db = sqlite3.connect('db/youdao.db')


    def init_user_db(self):
        self.table_name = 'user'
        self.db.execute("DROP TABLE IF EXISTS USER");
        self.db.execute('''CREATE TABLE USER
                   (ID  INT PRIMARY KEY    NOT NULL,
                    NAME           TEXT    NOT NULL,
                    EMAIL          TEXT    NOT NULL,
                    PASSWORD       TEXT    NOT NULL);
                   ''')

        self.add(1, 'ADMIN' , 'redorgreen@sina.cn', 'admin')

    def init_note_db(self):
        self.table_name = 'note'
        self.db.execute("DROP TABLE IF EXISTS NOTE");
        self.db.execute('''CREATE TABLE NOTE
                   (ID  INT PRIMARY KEY    NOT NULL,
                    NAME           TEXT    NOT NULL,
                    AUTHOR         INT     NOT NULL,
                    ISCOMMON       INT     NOT NULL,
                    SUB        CHAR(1000));
                   ''')

        self.add(1, 'YOUDAO-READEME' , 1, 1, 'YOUDAO-README.')

    def test_init(self):
        self.table_name = 'user'
        print('The first note\'s sub is equal = {sub}'.format(sub = self.select('JOIN NOTE WHERE AUTHOR = 1')[0][8]))


#init
i = initDbModel()

i.init_user_db()

i.init_note_db()

i.test_init()
# >>  python3 init_db.py
# The first note's sub is equal = YOUDAO-README.


