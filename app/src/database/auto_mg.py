from io import StringIO
from database.database import CursorFromConnectionPool


def create_from_file(df):
    """
    insert the csv data into auto_mg table.
    Parameters
    ----------
    df : dataframe
        dataframe to insert into the auto_mg table
    """
    # This method uses a buffer to load the csv file in an in-memory buffer and
    # copy it to the auto_mg table.
    # This methods proved to be faster than any most other methods
    df = df.fillna(0)
    # columns = tuple(df.columns)
    buffer = StringIO()
    df.to_csv(buffer, index_label='id', header=False)
    buffer.seek(0)
    with CursorFromConnectionPool() as cursor:
        cursor.copy_from(buffer, 'auto_mg', sep=',')
