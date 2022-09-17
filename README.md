[![Python application test with Github Actions using devcontainers](https://github.com/nogibjj/yayun_project01/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/yayun_project01/actions/workflows/main.yml)

# Keep tracks of lowest prices for wanted items with Databricks SQL Connector for Python 
![alt text](https://github.com/nogibjj/yayun_project01/blob/main/Blank%20board.png)

## Key objectives
This projects aims to keep track of the lowest prices of wanted items over several shopping websites with Databricks with Databricks SQL Connector.
Ideally, this project's goal is to provide a item's lowest prices summary as the follwoing:
```
Today's (2022-09-17) lowest price is: 
2650 USD at shopping website "net-a-porter."

The lowest price in past 30 days: 
2650 USD, at shopping website "net-a-porter" on 2022-09-17

The lowest price in past 60 days: 
2550 USD, at shopping website "mytheresa" on 2022-07-20

The lowest price in the record: 
2045 USD, at shopping website "net-a-porter" on 2021-09-13
```
Therefore, users can have a idea whether today is a good time to buy the item.



## Methodology
In this project, I chose YSL's solferino "small cross body bag" as my item and I used websites, "Saint Laurent", "SSENSE", "NET-A-PORTER", "MyTHERESA", "FARFETCH" as a example.
1. Everyday prices are collected by web-scrapping from these websites.
2. Create a table for this item and record its price everydat in Databricks with Databricks SQL Connector for Python.
3. Build CLI easily query tables in Databricks and get the item's lowest's price summary.
4. The Web App was created using FastAPI and uvicorn



## Files description

### scaffolding
* ```Makefille```: Compiling and configuration for the codespaces.
* ```requirements.txt```: pacakge used in this project.
* ```./devcontainer```: includes container files.

### web-scarpping
* ```websites_url.csv```: store urls of the wanted itmes on several interested websites.
* ```scrap_today_prcie```: python code for scrapping website in ```websites_url.csv``` to get the price of the wanted item.

### query Databricks table(./dblib)
* ```querydb```: python code for function for connection to Databricks and executing SQL query.
* ```insertdb```: python code for fucntion for conncetion to Databricks and ineserting data in to a table without needs to type full SQL query

### CLI
* ```query_sql_db.py```: python code for command line interface.

### Web-apps
* ```fastapi-app.py```: python code for a webframe work using fastAPI.
* ```get_prices```: python code for function used to get prices in ```fastapi-app.py```.




## User instruction
Type ```./query_sql_db.py --help``` to see the helper documentation.

### Using Command Line Interface

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

### Web-App

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











