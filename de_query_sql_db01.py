#!/usr/bin/env python

from cmd import PROMPT
from email.policy import default
import click
from dblib.querydb import querydb

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build  click commands
# query directly
@cli.command()
@click.option(
    "--query", default="SELECT * FROM default.diabetes LIMIT 3", help="SQL query to execute"
)
def cli_query(query):
    """Execute a SQL query"""
    querydb(query)


# query diabetes dataset based on input value
@cli.command()
@click.option("--age", default=0, prompt="Age Above", help="Age above")
@click.option("--gender", default= "1 | 2", prompt="Gender(male = 1, female = 2)")
@click.option("--bmi", default=0, prompt="BMI above")
@click.option( "--rows", default=3, prompt="Max Number of rows to return", help="Number of rows to return")

def cli_diabetes(age, gender, bmi, rows):
    """Query on a diabetes dataset automatically based on input values"""
    query = f"SELECT * FROM default.diabetes WHERE AGE > {age} AND SEX = {gender} AND BMI > {bmi} ORDER BY AGE  LIMIT {rows}"
    querydb(query)

# query mean blood biochemical level based on selected population
@cli.command()
@click.option("--age", default=0, prompt="Age Above", help="Age above")
@click.option("--gender", default="1 | 2", prompt="Gender(male = 1, female = 2")
@click.option("--bmi", default=0, prompt="BMI above")
@click.option("--biomarker", type=click.Choice(['TotalCholesterol', 'LDL', 'HDL', 'Glucose']), required = True, prompt = "biochemical marker")

def cli_meanbio(age, gender, bmi, biomarker):
    """Query mean blood biochemical level based on selected population"""
    query = f"SELECT AVG({biomarker}) FROM default.diabetes WHERE AGE >{age} AND SEX = {gender} AND BMI > {bmi}"
    querydb(query)


# run the CLI
if __name__ == "__main__":
    cli()
