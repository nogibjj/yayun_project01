from databricks import sql
import os

# insert data(less than thousands of rows)
def insertdb(table_name, insert_data, rows = 3):
    with sql.connect(
        server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
        http_path=os.getenv("DATABRICKS_HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_TOKEN"),
    ) as connection:

        with connection.cursor() as cursor:
            ## write a function that can assert the table exists
            cursor.execute(f"INSERT INTO {table_name} VALUES {insert_data}")
            cursor.execute(f"SELECT * FROM {table_name} LIMIT {rows}")
            result = cursor.fetchall()

            for row in result:
                print(row)
