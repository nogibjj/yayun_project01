from dblib.querydb import querydb
def get_prices(table):
    """Get the lowest prices of wanted items"""
    p = querydb(f'SELECT * FROM {table} ORDER BY date DESC LIMIT 1')[0]
    f1 = f'Today\'s ({p.date}) lowest prices is: "{p.LOWEST} USD at shopping websites "{p.BRANDS}."'   
    q_low_30 = f'SELECT date, LOWEST, BRANDS FROM (SELECT * FROM {table} ORDER BY date DESC LIMIT 30) WHERE LOWEST = (SELECT MIN(LOWEST) FROM (SELECT * FROM {table} ORDER BY date DESC LIMIT 30) LIMIT 1)'
    p1 = querydb(q_low_30)[0]
    f2 = f'The lowest price in past 30 days: {p1.LOWEST} USD, at shopping websites "{p1.BRANDS}" on {p1.date}.'
    q_low_60 = f'SELECT date, LOWEST, BRANDS FROM (SELECT * FROM {table} ORDER BY date DESC LIMIT 60) WHERE LOWEST = (SELECT MIN(LOWEST) FROM (SELECT * FROM {table} ORDER BY date DESC LIMIT 60) LIMIT 1)'
    p2 = querydb(q_low_60)[0]
    f3 = f'The lowest price in past 60 days: {p2.LOWEST} USD, at shopping websites "{p2.BRANDS}" on {p2.date}.'
    q_low_all = f'SELECT date, LOWEST, BRANDS FROM (SELECT * FROM {table} ORDER BY date DESC) WHERE LOWEST = (SELECT MIN(LOWEST) FROM (SELECT * FROM {table} ORDER BY date DESC) LIMIT 1)'
    p3 = querydb(q_low_all)[0]
    f4 = f'The lowest price in the record: {p3.LOWEST} USD, at shopping websites "{p3.BRANDS}" on {p3.date}.'   
    out = " ".join(["Collection the price of the YSL bag from 5 websites....,", f1, f2, f3, f4])
    return out
