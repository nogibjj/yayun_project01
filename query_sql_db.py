#!/usr/bin/env python

import click
from dblib.querydb import querydb
from dblib.insertdb import insertdb
from scrap_today_price import get_today_price


# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build  click commands for query directly
@cli.command()
@click.option(
    "--query",
    prompt = "enter your query",
    help="SQL query to execute",
)
def cli_query(query):
    """Execute a SQL query"""
    result = querydb(query)
    for row in result:
        print(row)


# build click commands for creating a new empty table
@cli.command()
@click.option(
    "--table_name",
    prompt="Table name",
    default="new_table",
    help="Table name to create",
)
@click.option(
    "--columns",
    default="col1 INT, col2 STRING",
    prompt="Column nanmes and type",
    help="Columns to create(enter: colname1 coltype1, colname2 coltype2,...etc)",
)
def cli_create(table_name, columns):
    """Create a new empty table"""
    querydb(f"CREATE TABLE {table_name} ({columns})")


# build click commands for inserting data into a table
@cli.command()
@click.option(
    "--table",
    required=True,
    prompt="Enter table name",
    help="Table name to insert data",
)
@click.option(
    "--data",
    required=True,
    prompt="Enter data: (col1, col2), (col1, col2)",
    help="Data to insert(enter a data list:(col1, col2), (col1, col2)",
)
@click.option(
    "--rows",
    default=3,
    prompt="Max Number of rows to return",
    help="Number of rows to return",
    type=int,
)
def cli_insert_data(table, data, rows):
    """Insert data into a table"""
    insertdb(table, data, rows)


# build click commands to get lowest prices of wanted items and insert today's prices to databricks database 
@cli.command()
@click.option("--table", prompt = "Enter table name")
def cli_enter_prices(table):
    """Get lowest prices of wanted items and insert today's prices to databricks database"""
    price = get_today_price()
    insertdb(table, price, 0)
    p = querydb(f'SELECT * FROM {table} ORDER BY date DESC LIMIT 1')[0]
    print(f"Today's ({p.date}) lowest price is: ")
    print(f'{p.LOWEST} USD at shopping websites "{p.BRANDS}."\n')
    q_low_30 = f'SELECT date, LOWEST, BRANDS FROM (SELECT * FROM {table} ORDER BY date DESC LIMIT 30) WHERE LOWEST = (SELECT MIN(LOWEST) FROM (SELECT * FROM {table} ORDER BY date DESC LIMIT 30) LIMIT 1)'
    p1 = querydb(q_low_30)[0]
    q_low_60 = f'SELECT date, LOWEST, BRANDS FROM (SELECT * FROM {table} ORDER BY date DESC LIMIT 60) WHERE LOWEST = (SELECT MIN(LOWEST) FROM (SELECT * FROM {table} ORDER BY date DESC LIMIT 60) LIMIT 1)'
    p2 = querydb(q_low_60)[0]
    q_low_all = f'SELECT date, LOWEST, BRANDS FROM (SELECT * FROM {table} ORDER BY date DESC) WHERE LOWEST = (SELECT MIN(LOWEST) FROM (SELECT * FROM {table} ORDER BY date DESC) LIMIT 1)'
    p3 = querydb(q_low_all)[0]
    print(f'The lowest price in past 30 days: \n{p1.LOWEST} USD, at shopping websites "{p1.BRANDS}" on {p1.date}\n')
    print(f'The lowest price in past 60 days: \n{p2.LOWEST} USD, at shopping websites "{p2.BRANDS}" on {p2.date}\n')
    print(f'The lowest price in the record: \n{p3.LOWEST} USD, at shopping websites "{p3.BRANDS}" on {p1.date}\n')


@cli.command()
@click.option("--table", prompt = "Enter table name")
def cli_get_prices(table):
    """Get lowest prices of wanted items"""
    p = querydb(f'SELECT * FROM {table} ORDER BY date DESC LIMIT 1')[0]
    print(f"Today's ({p.date}) lowest price is: ")
    print(f'{p.LOWEST} USD at shopping websites "{p.BRANDS}."\n')
    q_low_30 = f'SELECT date, LOWEST, BRANDS FROM (SELECT * FROM {table} ORDER BY date DESC LIMIT 30) WHERE LOWEST = (SELECT MIN(LOWEST) FROM (SELECT * FROM {table} ORDER BY date DESC LIMIT 30) LIMIT 1)'
    p1 = querydb(q_low_30)[0]
    q_low_60 = f'SELECT date, LOWEST, BRANDS FROM (SELECT * FROM {table} ORDER BY date DESC LIMIT 60) WHERE LOWEST = (SELECT MIN(LOWEST) FROM (SELECT * FROM {table} ORDER BY date DESC LIMIT 60) LIMIT 1)'
    p2 = querydb(q_low_60)[0]
    q_low_all = f'SELECT date, LOWEST, BRANDS FROM (SELECT * FROM {table} ORDER BY date DESC) WHERE LOWEST = (SELECT MIN(LOWEST) FROM (SELECT * FROM {table} ORDER BY date DESC) LIMIT 1)'
    p3 = querydb(q_low_all)[0]
    print(f'The lowest price in past 30 days: \n{p1.LOWEST} USD, at shopping websites "{p1.BRANDS}" on {p1.date}\n')
    print(f'The lowest price in past 60 days: \n{p2.LOWEST} USD, at shopping websites "{p2.BRANDS}" on {p2.date}\n')
    print(f'The lowest price in the record: \n{p3.LOWEST} USD, at shopping websites "{p3.BRANDS}" on {p1.date}\n')


# run the CLI
if __name__ == "__main__":
    cli()
