import psycopg2
from psycopg2 import *
from utils import *

log_type = "conn"

class Connect:
    def __init__(self) -> None:
        pass
    
    _i = None # Connect object

    def __new__(x): # runs everytime a Connect object is created
        if x._i is None: # if there is no Connect object
            x._i = super(Connect, x).__new__(x) # create a new object
            try:
                # create a connection to the database
                x._i.conn = psycopg2.connect( dbname = "DBing_sftw", user = "stek", password = "stek765", host = "localhost")
                # create a cursor
                x._i.cursor = x._i.conn.cursor()
            except OperationalError as e:
                Log("model",f"@__new__: errore durante la connessione al database: {e}")
        return x._i
    
    def execute_query(self, query, parameters=None):
        try:
            self.cursor.execute(query) # execute query

            if self.cursor.description is not None:
                result = self.cursor.fetchall() # fetch all rows
                self.conn.commit() # commit
                return result # return fetched rows
            elif query.strip().upper().startswith(("INSERT","UPDATE","DELETE")):
                self.conn.commit() # commit
                return True
            else:
                return None
        except Exception as e:
            Log("model",f"@execute_query: error: {e}")
            return None

    def close_connection(self):
        if self.conn:
            try:
                self.cursor.close()
                self.conn.close()
            except Exception as e:
                Log("model",f"@close_connection: Error: {e}")

class Model:
    def __init__(self):
        self.db_conn:Connect = Connect()

    def get_data(self, _select="*", _from="", _where=1, _equals=1):
        return self.db_conn.execute_query(f"SELECT {_select} FROM {_from} WHERE {_where} = '{_equals}';")

    def print_data(self,data):
        [print(i) for i in data]

    

if __name__ == '__main__':
    model = Model()
    data = model.get_data("*","medico")
    model.print_data(data)