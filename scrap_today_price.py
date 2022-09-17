from datetime import date
from requests_html import HTMLSession

url_dict = {
            'ssense':'https://www.ssense.com/en-us/women/product/saint-laurent/taupe-small-solferino-bag/9118391',
            'net-a-porter':'https://www.net-a-porter.com/en-us/shop/product/saint-laurent/bags/cross-body/solferino-small-leather-shoulder-bag/6630340696680927',
            'farfetch':'https://www.farfetch.com/shopping/women/saint-laurent-small-solferino-crossbody-bag-item-16360071.aspx?fsb=1&size=17&storeid=13824',
            'mytheresa': 'https://www.mytheresa.com/en-us/saint-laurent-solferino-small-leather-crossbody-bag-1840157.html',
            'official_ysl':'https://www.ysl.com/en-us/satchel-and-bucket-bags/solferino-small-satchel-in-box-saint-laurent-leather-6343060SX0W2357.html'
            }

user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
def get_price_ssense(url,s = HTMLSession()):
    r = s.get(url, headers = {'User-Agent': user})
    price = r.html.find('h3#pdpRegularPriceText',  first = True).text
    price = int(price[1:-4])
    return price
    
def get_price_netA(url,s = HTMLSession()):
    r = s.get(url, headers = {'User-Agent': user})
    price = r.html.find('div.PriceWithSchema9.PriceWithSchema9--details.ProductDetails85__price span.PriceWithSchema9__value.PriceWithSchema9__value--details span', first = True).text
    price = int(price[1:].replace(",",""))
    return price  

def get_price_farfetch(url, s = HTMLSession()):
    r = s.get(url, headers = {'User-Agent': user})
    price = r.html.find('p.ltr-194u1uv-Heading.e54eo9p0', first = True).text
    price = int(price[1:].replace(",",""))
    return price

def get_price_mytheresa(url, s = HTMLSession()):
    r = s.get(url, headers = {'User-Agent': user})
    price = r.html.find('span.price', first = True).text
    price = int(price[2:].replace(",",""))
    return price

def get_price_ysl(url, s = HTMLSession()):
    r = s.get(url, headers = {'User-Agent': user})
    price = r.html.find('p.c-price__value--current', first = True).text
    price = int(price[2:].replace(',',""))
    return price

def get_today_price():
    today = date.today().strftime("%Y-%m-%d")
    lis = [today]  
    lis.append(get_price_ysl(url_dict['official_ysl']))
    lis.append(get_price_ssense(url_dict['ssense']))
    lis.append(get_price_netA(url_dict['net-a-porter']))
    lis.append(get_price_farfetch(url_dict['farfetch']))
    lis.append(get_price_mytheresa(url_dict['mytheresa']))
    today_min = min(lis[1:])
    lis.append(today_min)
    brand_list = ['official_ysl', 'ssense', 'net-a-porter', 'farfetch', 'mytheresa']
    min_brands = [brand_list[i] for i in range(len(brand_list)) if lis[i+1] == today_min]
    lis.append(", ".join(min_brands))
    values = f'{tuple(lis)}'
    return values







    
