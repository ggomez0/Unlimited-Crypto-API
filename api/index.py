from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def about():
    with open('api/webpage.html', 'r') as file:
        content = file.read()
    return content

@app.route('/favicon.png')
def favicon():
    with open('api/btc.png', 'rb') as file:
        content = file.read()
    return content, 200, {'Content-Type': 'image/png'}

@app.route('/api/price/<string:item_id>')
def request_page(item_id):
    soup = get_url('https://www.coingecko.com/en/coins/' + item_id)
    price_element = soup.find('span', {'data-converter-target': 'price'})
    
    if price_element:
        price = price_element.text.strip() 
        print(f"Precio de {item_id}:", price)
        json = {'coin': item_id, 
            'price': price}
        return json
    else:
        print("No se encontró el precio.")
        return 'No se encontró el precio.'

@app.route('/api/top_coins_markets/<int:limit>')
def top_coins_markets(limit=1):
    json = []
    
    soup = get_url('https://www.coingecko.com/')
    rows = soup.find_all('tr', {'class': 'hover:tw-bg-gray-50 tw-bg-white dark:tw-bg-moon-900 hover:dark:tw-bg-moon-800 tw-text-sm'})
    rows = rows[:limit]
    
    for row in rows:
        name = row.find('div', {'class': 'tw-text-gray-700 dark:tw-text-moon-100 tw-font-semibold tw-text-sm tw-leading-5'}).contents[0].strip()
        symbol = row.find('div', {'class': 'tw-block 2lg:tw-inline tw-text-xs tw-leading-4 tw-text-gray-500 dark:tw-text-moon-200 tw-font-medium'}).text.strip()
        price = row.find('td', {'data-sort': True}).span.text.strip()
        image = row.find('img', {'class': 'tw-mr-2 !tw-h-6 tw-w-6 tw-object-fill'})['src']
        
        json.append(
            {'name': name, 
             'symbol': symbol, 
             'price': price, 
             'image':image
             })
    return json
    

def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
