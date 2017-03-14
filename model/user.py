from lib.query import Query

class UserModel(Query):
    def __init__(self, conn):
        self.conn = conn
        self.table_name = "user"
        super(UserModel, self).__init__()

    def test_conn(self):
        conn = self.conn
        conn.execute('''CREATE TABLE COM
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            ADDRESS        CHAR(50),
            SALARY         REAL);
            ''')

        conn.execute("INSERT INTO COM (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )");

        conn.commit()
        cursor = conn.execute("SELECT * FROM COM")
        print('list(cursor) = \n')
        print(list(cursor))
        conn.execute("DROP TABLE COM");
