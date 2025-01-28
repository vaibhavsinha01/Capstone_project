import yfinance as yf 
import matplotlib.pyplot as plt 

# stocks = ['AAPL', 'MSFT', 'NVDA', 'GOOGL']
# stocks = ['AAPL', 'MSFT', 'NVDA', 'GOOGL', 'AMZN', 'TSLA', 'META', 'SPY', 'V', 'JPM', 'DIS', 'INTC', 'CSCO', 'NFLX', 'PYPL', 'BA', 'IBM', 'WMT', 'KO', 'PFE', 'MA']
stocks = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS', 'SBIN.NS', 'HINDUNILVR.NS', 'KOTAKBANK.NS','AXISBANK.NS','BAJFINANCE.NS', 'BAJAJFINSV.NS', 'MARUTI.NS', 'ASIANPAINT.NS', 'HDFCLIFE.NS', 'TITAN.NS', 'WIPRO.NS', 'ULTRACEMCO.NS', 'SUNPHARMA.NS','ONGC.NS', 'TATAMOTORS.NS', 'POWERGRID.NS', 'HDFCBANK.NS', 'TCS.NS', 'ITC.NS', 'JSWSTEEL.NS','TATACONSUM.NS', 'ADANIGREEN.NS', 'ADANIPORTS.NS','BAJFINANCE.NS', 'BAJAJFINSV.NS', 'MARUTI.NS', 'ASIANPAINT.NS','HDFCLIFE.NS', 'TITAN.NS', 'WIPRO.NS', 'ULTRACEMCO.NS', 'SUNPHARMA.NS', 'HCLTECH.NS','ONGC.NS', 'TATAMOTORS.NS','TATASTEEL.NS']
lookback = 50
values = []
def McClellan_Indicator_Score(stocks,daysback):
    advance = 0
    decline = 0
    for stock in stocks:
        data = yf.download(stock, period="1y", interval="1d")
        last_close = data['Close'].iloc[-daysback].item()  
        last_open = data['Open'].iloc[-daysback].item()    
        
        if last_close > last_open:
            advance += 1
        elif last_close < last_open:
            decline += 1
    
    return (advance - decline) / (advance + decline)

for i in range(lookback,0,-1):
    SCORE = McClellan_Indicator_Score(stocks,i)
    values.append(SCORE)

plt.plot(values)
plt.savefig('nifty50.png')
plt.show()
