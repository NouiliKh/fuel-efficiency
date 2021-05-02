from io import StringIO
from database.database import CursorFromConnectionPool


class CRUDFromDf:
    def __init__(self, df, table_name):
        self.df = df.fillna(0)
        self.columns = tuple(df.columns)
        self.table_name = table_name

    def create_from_file(self):
        buffer = StringIO()
        self.df.to_csv(buffer, index_label='id', header=False)
        buffer.seek(0)
        with CursorFromConnectionPool() as cursor:
            cursor.copy_from(buffer, self.table_name, sep=',')
