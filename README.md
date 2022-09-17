[![Python application test with Github Actions using devcontainers](https://github.com/nogibjj/yayun_project01/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/yayun_project01/actions/workflows/main.yml)

# Keep tracks of the lowest prices for wanted items everyday with Databricks SQL Connector for Python 
![alt text](https://github.com/nogibjj/yayun_project01/blob/main/Blank%20board.png)

# Key objectives
This projects aims to keep track of the lowest prices of my wanted item over several shopping websites.



# Demo Video

# Methodology
In this project, for example, I chose YSL's solferino "small cross body bag" as my item and I used websites, "Saint Laurent", "SSENSE", "NET-A-PORTER", "MyTHERESA", "FARFETCH". I scrapped the item's prices from these websites and stored into Databricks table. 

# Files description

## web-scarpping
* websites_url.csv: store urls of the wanted itmes on several interested websites.
* URLs of shopping websites for the wanted item (a ysl bag)

## helper




# User instruction
Type ```./query_sql_db.py --help``` to see the helper documentation.

## Using Command Line Interface

#### Record everyday price and get report of the lowest prices
Here, I chose YSL's solferino "small cross body bag" for example. 

* First, store website url for your wanted-item. as a csv file in your repository. (ex. website_url.csv)
* Second, create a table in databricks to store your data.   
Run ```./query_sql_db.py cli-create```.Type the table name, and then specify column name (date, website, lowest price, website for lowest price today) and type as the following in the command line. If you enter correctly, it should return "This is a empty table"

Here is the example:
```
$ ./query_sql_db.py cli-create
Table name [new_table]: wanted_item
Column nanmes and type [col1 INT, col2 STRING]: date DATE, YSL INT, SSENSE INT, NETA INT, FARFETCH INT, MYTHERESA INT, LOWEST INT, BRANDS STRING
This is a empty table.
```
* Third, keep every day prices and get every day summary. 
Run ```./query_sql_db.py cli-enter-prices```. Enter table name. If enter correctly, it should return the lowest prices of today and over past 30, 60 days and all records.   
*\*\*\*Remeber, when you type ```./query_sql_db.py cli-get-prices```, today's prices will also be recorded into Databricks table. If you have already recorded and just want to see today's price summary, use ```./query_sql_db.py cli-get-prices``` instead.*

Here is the example: (This is just an example, not the real price!)
```
$ ./query_sql_db.py cli-get-prices
Enter table name: wanted_item

Today's (2022-09-17) lowest price is: 
2650 USD at shopping websites "net-a-porter."

The lowest price in past 30 days: 
2650 USD, at shopping websites "net-a-porter" on 2022-09-17

The lowest price in past 60 days: 
2550 USD, at shopping websites "mytheresa" on 2022-07-20

The lowest price in the record: 
2045 USD, at shopping websites "net-a-porter" on 2021-09-13

```
---------------------------------------------
#### Query, Create, Insert Databricks table
Directly query any table in Databricks with SQL query.
Type:```./query_sql_db.py cli-query``` Then enter your query like ``` SELECT * FROM wanted_item LIMIT 3```.



**Without knowing how to write a SQL query**, create, insert data into table using simplified command line inputs.
Type ```./query_sql_db.py cli-insert-data``` to insert data and Type ```./query_sql_db.py cli-create``` to create table. For example:

```
$ ./query_sql_db.py cli-insert-data
Enter table name: wanted_item
Enter data: (col1, col2), (col1, col2): ('2022-03-22', 2030, 2050, 2010, 2007, 2090, 2030, 'test-insert')
Max Number of rows to return [3]: 1

Row(date=datetime.date(2022, 3, 3), YSL=2000, SSENSE=2030, NETA=2050, FARFETCH=2010, MYTHERESA=2007, LOWEST=2030, BRANDS='test')
```

## Web-App

Code needed to run the web app using FastAPI are in fastapi. To run the web app, type in ```python fastapi-app.py``` in your terminal and open up the web app on a new tab on your browser. This should take you to a website showing "Hi there, please enter '/get_prices/table_name' after current url to find the lowest prices of it! (it may take a few seconds to load the page)"

You can then type ```get_prices/{tablenName for the item}``` after current url to get today's price summary for the item you want to know.
For example:  
Enter ```https://yayunyun-nogibjj-yayun-project01-4567g4wjr56h55j9-8080.githubpreview.dev/get_prices/wanted_item```. 
will get a result like:
```
"Collection the price of the YSL bag from 5 websites...., 
Today's (2022-09-17) lowest prices is: \"2650 USD at shopping websites \"net-a-porter.\" 
The lowest price in past 30 days: 2650 USD, at shopping websites \"net-a-porter\" on 2022-09-17. 
The lowest price in past 60 days: 2650 USD, at shopping websites \"net-a-porter\" on 2022-09-17. 
The lowest price in the record: 2650 USD, at shopping websites \"net-a-porter\" on 2022-09-17."
```



### Other query








