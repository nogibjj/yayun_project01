#!/usr/bin/env python

from cmd import PROMPT
from email.policy import default
import click
from dblib.querydb import querydb
from dblib.insertdb import insertdb

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build  click commands for query directly
@cli.command()
@click.option(
    "--query",
    default="SELECT * FROM default.diabetes LIMIT 3",
    help="SQL query to execute",
)
def cli_query(query):
    """Execute a SQL query"""
    querydb(query)

# build click commands for creating a new empty table
@cli.command()
@click.option("--table_name", default="new_table", help="Table name to create")
@click.option("--columns", default="col1 INT, col2 STRING", help="Columns to create(enter: colname1 coltype1, colname2 coltype2,...etc)")
def cli_create_table(table_name, columns):
    """Create a new empty table"""
    querydb(f"CREATE TABLE {table_name} ({columns})")

# build click commands for inserting data into a table
@cli.command()
@click.option("--table", required = True, prompt = "Enter table name", help="Table name to insert data")
@click.option("--data", required = True, prompt = "Enter data" ,help="Data to insert(enter a data list:(col1, col2), (col1, col2)")
@click.option("--rows",default=3, prompt="Max Number of rows to return",help="Number of rows to return",type=int)
def cli_insert_data(table, data, rows):
    """Insert data into a table"""
    insertdb(table, data, rows)

# build click commands to add data from python
@cli.command()
@click.option("--scrap", required = True ,help="dataset to scrap")
@click.option("--table", required = True, prompt = "Enter table name", help="Table name to insert data")
@click.option("--rows",default=3, prompt="Max Number of rows to return",help="Number of rows to return",type=int)
def cli_insert_python_data(data, table, rows):
    insert_data = scrap() # should return formatted data
    """Insert data into a table"""
    insertdb(table, insert_data, rows)


# run the CLI
if __name__ == "__main__":
    cli()
