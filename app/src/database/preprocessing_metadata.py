from database.database import CursorFromConnectionPool


def create_from_dict(dict):
    """
    insert the data dictionary into preprocessing_metadata table.
    Parameters
    ----------
    dict : dictionary
        dictionary to insert into the preprocessing_metadata table
    """
    with CursorFromConnectionPool() as cursor:
        cols = dict.keys()
        cols_str = ','.join(cols)
        vals = [dict[x] for x in cols]
        vals_str_list = ["%s"] * len(vals)
        vals_str = ", ".join(vals_str_list)

        sql_str = """INSERT INTO preprocessing_metadata ({}) VALUES ({})""".format(cols_str, vals_str)
        cursor.execute(sql_str, vals)

