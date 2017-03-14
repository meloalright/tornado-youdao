from lib.query import Query

class UserModel(Query):
    def __init__(self, conn):
        self.conn = conn
        self.table_name = "user"
        super(UserModel, self).__init__()

    def test_conn(self):
        conn = self.conn
        conn.execute("DROP TABLE IF EXISTS TEST");
        conn.execute('''CREATE TABLE TEST
            (ID INT PRIMARY KEY     NOT NULL,
            NAME           TEXT    NOT NULL,
            SUB        CHAR(50));
            ''')

        conn.execute("INSERT INTO TEST (ID,NAME,SUB) VALUES (1, 'YOUDAO', 'TEST OK' )");

        conn.commit()
        cursor = conn.execute("SELECT * FROM TEST")
        print(list(cursor))
        conn.execute("DROP TABLE TEST");
