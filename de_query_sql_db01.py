#!/usr/bin/env python

from cmd import PROMPT
from email.policy import default
import click
from dblib.querydb import querydb

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build a click command
@cli.command()
@click.option("--age", default=0, prompt="Age Above", help="Age above")
@click.option("--gender", default="1 | 2", prompt="Gender(male = 1, female = 2")
@click.option("--bmi", default=0, prompt="BMI above")
@click.option(
    "--rows",
    default=3,
    prompt="Number of rows to return",
    help="Number of rows to return",
)
def cli_diabetes(age, gender, bmi, rows):
    """Execute a query on azureml diabetes open dataset automatically based on your input values"""
    query = f"SELECT * FROM diabetes WHERE AGE > {age} AND SEX = {gender} AND BMI > {bmi} ORDER BY AGE  LIMIT {rows}"
    querydb(query)


# query directly
@cli.command()
@click.option(
    "--query", default="SELECT * FROM diabetes LIMIT 3", help="SQL query to execute"
)
def cli_query(query):
    """Execute a SQL query"""
    querydb(query)


# run the CLI
if __name__ == "__main__":
    cli()
