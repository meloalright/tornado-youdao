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


    def add(self, sup):
        self.db.execute("INSERT INTO {table} {sup}".format(table=self.table_name, sup=sup))
        self.db.commit()

    def select(self, filt=''):
        return list(self.db.execute("SELECT * FROM {table} {filt}".format(table=self.table_name, filt=filt)))

    def select_one(self, filt=''):
        try:
            return list(self.db.execute("SELECT * FROM {table} {filt}".format(table=self.table_name, filt=filt)))[0]
        except:
            return None

    def execute(self, sup):
        return list(self.db.execute(sup))

    def update(self, set_filt=''):
        self.db.execute("UPDATE {table} {set_filt}".format(table=self.table_name, set_filt=set_filt))
        self.db.commit()


    def delete(self, filt=''):
        self.db.execute("DELETE FROM {table} {filt}".format(table=self.table_name, filt=filt))
        self.db.commit()




