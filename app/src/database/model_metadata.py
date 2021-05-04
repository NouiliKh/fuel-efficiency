from database.database import CursorFromConnectionPool


def create_from_dict(dict):
    """
    insert the data dictionary into model_metadata table.
    Parameters
    ----------
    dict : dictionary
        dictionary to insert into the auto_mg table
    """
    with CursorFromConnectionPool() as cursor:
        cols = dict.keys()
        cols_str = ','.join(cols)
        vals = [dict[x] for x in cols]
        vals_str_list = ["%s"] * len(vals)
        vals_str = ", ".join(vals_str_list)

        sql_str = """INSERT INTO model_metadata ({}) VALUES ({})""".format(cols_str, vals_str)
        cursor.execute(sql_str, vals)


def fetch_model_with_accuracy_threshold(accuracy_threshold):
    """
    fetches the models with an accuracy higher than a certain threshold.
    Parameters
    ----------
    accuracy_threshold : threshold
        threshold to be considered
    """
    with CursorFromConnectionPool() as cursor:
        sql_str = """SELECT * FROM model_metadata WHERE mae_test < ({}) AND created_at >= current_date - interval '7 days'""".format(accuracy_threshold)
        cursor.execute(sql_str)
        return cursor.fetchall()
