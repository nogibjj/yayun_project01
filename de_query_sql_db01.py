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
@click.option("--age", default = 0, prompt="Age Above", help="Age above")
@click.option("--gender", default = "1 | 2", prompt = "Gender(male = 1, female = 2")
@click.option("--bmi", default = 0, prompt = "BMI above")
@click.option("--rows", default = 3, prompt="Number of rows to return", help="Number of rows to return")

def cli_query(age, gender, bmi, rows):
    """Execute a SQL query on azureml diabetes open dataset"""
    query = f"SELECT * FROM default.diabetes WHERE AGE > {age} AND SEX = {gender} AND BMI > {bmi} ORDER BY AGE  LIMIT {rows}"
    querydb(query)


# run the CLI
if __name__ == "__main__":
    cli()
