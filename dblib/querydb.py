from databricks import sql
import os


def querydb(query = 'SELECT * FROM default.diabetes_csv LIMIT 3'):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        if len(result) == 0:
            print("This is a empty table")
        else:
            pass

    return result