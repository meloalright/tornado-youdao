#query.py
import re



class Query(object):
    def __init__(self, table_name = None, db = None):
        if not table_name == None:
            self.table_name = table_name

        if not db == None:
            self.db = db

        self.__reset()
        
    def __reset(self):
        pass

    def __close(self):
        pass

    def add(self, values):
        self.db.execute("INSERT INTO %s VALUES %s"% (self.table_name ,values))
        self.db.commit()

    def show_all(self):
        print(list(self.db.execute("SELECT * FROM %s"% (self.table_name))))

