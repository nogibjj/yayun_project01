from fastapi import FastAPI
import uvicorn
from get_prices import get_prices
from dblib.querydb import querydb

app = FastAPI()


@app.get("/")
async def root():
    return  "Hi there, please enter '/my_ysl_bag' after current url to find the lowest prices of it! (it may take a few seconds to load the page)"

@app.get("/my_ysl_bag")
async def wanted_item():
    """Get the lowest price for the wanted_item"""
    result = get_prices()
    return result

@app.get("/query")
async def query():
    """Execute a SQL query"""

    result = querydb()
    return {"result": result}



if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
