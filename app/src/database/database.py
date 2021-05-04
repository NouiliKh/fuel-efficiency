from psycopg2 import pool


class Database:
    """
    A class used to handle database connection by initializing the connection pool first.
    ...
    Methods
    -------
    initialise()
        initialises the connection to the database
    get_connection()
        retrieves the connection initialized
    return_connection(connection)
        puts away the connection
    """
    __connection_pool = None

    @staticmethod
    def initialise(**kwargs):
        """
        initialises the connection to the database
        Parameters
        ----------
        database: str
            database name
        user: str
            database user name
        password: str
            database password
        host str:
            database address
        """
        Database.__connection_pool = pool.SimpleConnectionPool(1, 10, **kwargs)

    @staticmethod
    def get_connection():
        """
        retrieves the connection initialized
        """
        return Database.__connection_pool.getconn()

    @staticmethod
    def return_connection(connection):
        """
        puts away the connection
        """
        Database.__connection_pool.putconn(connection)


class CursorFromConnectionPool:
    """
    A class used to handle database transactions: retrieved when entering and close while exiting if no problems
    else rollback.
    ...
    Attributes
    ----------
    conn:
        database connection
    cursor:
        database cursor
    ...
    Methods
    -------
    __init__()
        initialises the connection and the cursor.
    __enter__()
        returns the cursor while using this class
    __exit__(connection)
        commits the transaction if successful and rollbacks if not.
    """

    # Here I have the possibility to get the connection once every transaction is made or only the first time
    def __init__(self):
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = Database.get_connection()
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value:  # This is equivalent to `if exception_value is not None`
            self.conn.rollback()
        else:
            self.cursor.close()
            self.conn.commit()
        Database.return_connection(self.conn)