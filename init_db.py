#init_db.py
from lib.query import Query
from model.user import UserModel
from model.note import NoteModel
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
        um = UserModel(self.db)
        um.sign_up_object('melo', 'redorgreen@sina.cn', '999999')
        print(um.valid_user('mez', '123456'))
        print(um.valid_user('melo', '123456'))
        print(um.valid_user('melo', '999999'))
        user = um.valid_user('melo', '999999')
        um.update_password(user['id'], '000000')
        print(um.valid_user('melo', '000000'))

        nm = NoteModel(self.db)
        nm.create_note_object('melo \'s first note', 1, 1, 'This is melo \'s first note')
        nm.create_note_object('melo \'s second note', 1, 1, 'This is melo \'s second note')
        nm.set_uncommon(2)
        nm.update_note(1, 'Melo \'s first note', 'This is melo \'s first note yeah')
        print(nm.get_note(1))
        print(nm.get_note(2))
        print(um.get_user_note_list(1))


#init
i = initDbModel()

i.init_user_db()

i.init_note_db()

i.test_init()
# >>  python3 init_db.py



