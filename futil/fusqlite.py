import sqlite3


class CheckReg():
    '''
    The CheckReg class checks for reg class connects to db and has a method which checks it
    '''
    def __init__(self, path_db):
        self.connection = sqlite3.connect(path_db)
        self.cursor = self.connection.cursor()

    def n_tables(self):
        n_tab = len(self.cursor.execute("""SELECT name FROM sqlite_master where type = 'table'""").fetchall())
        return n_tab

    #def table_name(self): 

    #def reg_nr_exists(self, )
    def check_reg(self, table, column, reg_nr):
        self.reg_exists = self.cursor.execute(("""SELECT 1 FROM {} WHERE {} = '{}'""").format(table, column, reg_nr)).fetchall()


    # Various methods to check can be written here might be a good idea to just use pd.read_sql since then you have nice tables right away


    def __del__(self):
        self.cursor.close()
        self.connection.close()

