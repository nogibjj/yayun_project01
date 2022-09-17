[![Python application test with Github Actions using devcontainers](https://github.com/nogibjj/yayun_project01/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/yayun_project01/actions/workflows/main.yml)

# Keep tracks of the lowest prices for wanted items everyday with Databricks SQL Connector for Python 

# Key objectives
This projects aims to 
that people who have do not understand SQL syntax can also use.


# Demo Video

# Methodology

# Files description

## web-scarpping
URLs of shopping websites for the wanted item (a ysl bag)

## helper




# User instruction
Type ```./query_sql_db.py --help``` to see the helper documentation.

## Using Command Line Interface

#### Record everyday price and get report of the lowest prices
Here, I chose YSL's solferino "small cross body bag" for example. 

* First, store website url for your wanted-item. as a csv file in your repository. (ex. website_url.csv)
* Second, create a table in databricks to store your data.
Type `cli-create`


First, create a table to store your data. 

```
$ ./query_sql_db.py cli-create







### Other query








