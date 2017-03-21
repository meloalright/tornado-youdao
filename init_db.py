#init_db.py
from lib.query import Query
from model.user import UserModel
import sqlite3
import redis

conn = redis.Redis(host='127.0.0.1', port=6379)

class initDbModel(Query):
    def __init__(self):
        super(initDbModel, self).__init__()
        self.db = sqlite3.connect('db/youdao.db')


    def init_user_db(self):
        self.table_name = 'user'
        self.db.execute("DROP TABLE IF EXISTS USER");
        self.db.execute('''CREATE TABLE USER
                   (ID  integer PRIMARY KEY autoincrement,
                    NAME           TEXT    NOT NULL,
                    EMAIL          TEXT    NOT NULL,
                    PASSWORD       TEXT    NOT NULL);
                   ''')


    def init_note_db(self):
        self.table_name = 'note'
        self.db.execute("DROP TABLE IF EXISTS NOTE");
        self.db.execute('''CREATE TABLE NOTE
                   (ID  integer PRIMARY KEY autoincrement,
                    NAME           TEXT    NOT NULL,
                    AUTHOR         INT     NOT NULL,
                    ISCOMMON       INT     NOT NULL,
                    SUB        CHAR(1000));
                   ''')


    def test_init(self):
        '''
         model test
        '''
        um = UserModel(sqlite3.connect('db/youdao.db'))
        um.sign_up_object('melo', 'redorgreen@sina.cn', '999999')
        print(um.valid_password('melo', '999999'))

#init
i = initDbModel()

i.init_user_db()

i.init_note_db()

i.test_init()
# >>  python3 init_db.py



