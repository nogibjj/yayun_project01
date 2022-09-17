from fastapi import FastAPI
import uvicorn
from get_prices import get_prices
from dblib.querydb import querydb

app = FastAPI()


@app.get("/")
async def root():
    return  "Hi there, please enter '/get_prices/table_name' after current url to find the lowest prices of it! (it may take a few seconds to load the page)"

@app.get("/get_prices/{table}")
async def wanted_item(table: str):
    """Get the lowest price for the wanted_item"""
    result = get_prices(table)
    return result

@app.get("/query/{queryx}")
async def query(queryx: str):
    """Execute a SQL query"""

    result = querydb(queryx)
    return {"result": result}



if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
