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

    def add(self, *args):
        values = args
        self.db.execute("INSERT INTO {table} VALUES {kwarg}".format(table=self.table_name, kwarg=values))
        self.db.commit()


    def select(self, filt=''):
        return list(self.db.execute("SELECT * FROM {table} {filt}".format(table=self.table_name, filt=filt)))

    def show_all(self):
        print(list(self.db.execute("SELECT * FROM %s"% (self.table_name))))

