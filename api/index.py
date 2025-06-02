from flask import Flask
import ccxt

app = Flask(__name__)

exchange = ccxt.binance({
    'enableRateLimit': True,
    'options': {
        'defaultType': 'spot',
    }
})

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


@app.route('/api/price/<string:symbol>')
def get_binance_price(symbol):
    try:
        ticker = exchange.fetch_ticker(symbol.upper() + '/USDT')
        return {
            'symbol': symbol.upper(),
            'price': ticker['last'],
            'volume_usdt': ticker['quoteVolume'],
            'change_24h': ticker['percentage']
        }
    except Exception as e:
        return {'error': str(e)}
    
@app.route('/api/top/<int:limit>')
def get_top_cryptos(limit):
    try:
        tickers = exchange.fetch_tickers()
        
        usdt_markets = []
        for symbol, ticker in tickers.items():
            par = symbol.split('/')
            if 'USD' in par[0]:
                continue
            if symbol.endswith('/USDT'):
                market_data = {
                    'symbol': symbol.replace('/USDT', ''),
                    'price': ticker['last'],
                    'volume_usdt': ticker['quoteVolume'],
                    'change_24h': ticker['percentage']
                }
                usdt_markets.append(market_data)
        
        sorted_markets = sorted(usdt_markets, key=lambda x: x['volume_usdt'] if x['volume_usdt'] else 0, reverse=True)
        
        return {
            'top_cryptos': sorted_markets[:limit]
        }
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
