from dblib.querydb import querydb
def get_prices():
    """Get the lowest prices of wanted items"""
    p = querydb('SELECT * FROM wanted_item ORDER BY date DESC LIMIT 1')[0]
    f1 = f'Today\'s lowest prices is: "{p.LOWEST} USD at shopping websites "{p.BRANDS}."'
    q_low_30 = 'SELECT date, LOWEST, BRANDS FROM (SELECT * FROM wanted_item ORDER BY date DESC LIMIT 30) WHERE LOWEST = (SELECT MIN(LOWEST) FROM (SELECT * FROM wanted_item ORDER BY date DESC LIMIT 30) LIMIT 1)'
    p1 = querydb(q_low_30)[0]
    q_low_60 = 'SELECT date, LOWEST, BRANDS FROM (SELECT * FROM wanted_item ORDER BY date DESC LIMIT 60) WHERE LOWEST = (SELECT MIN(LOWEST) FROM (SELECT * FROM wanted_item ORDER BY date DESC LIMIT 60) LIMIT 1)'
    p2 = querydb(q_low_60)[0]
    q_low_all = 'SELECT date, LOWEST, BRANDS FROM (SELECT * FROM wanted_item ORDER BY date DESC) WHERE LOWEST = (SELECT MIN(LOWEST) FROM (SELECT * FROM wanted_item ORDER BY date DESC) LIMIT 1)'
    p3 = querydb(q_low_all)[0]
    f2 = f'The lowest price in past 30 days: {p1.LOWEST} USD, at shopping websites "{p1.BRANDS}" on {p1.date}.'
    f3 = f'The lowest price in past 60 days: {p2.LOWEST} USD, at shopping websites "{p2.BRANDS}" on {p2.date}.'
    q_count = 'SELECT COUNT(*) FROM wanted_item'
    f4 = f'The lowest price in past {querydb(q_count)[0].count(1)} days: {p3.LOWEST} USD, at shopping websites "{p3.BRANDS}" on {p1.date}.'
    out = " ".join(["Collection the price of the YSL bag from 5 websites....,", f1, f2, f3, f4])
    return out
