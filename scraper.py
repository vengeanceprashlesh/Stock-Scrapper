import yfinance as yf

def get_stock_data(tickers):
    """
    Fetches stock data and news for the given tickers.
    
    Args:
        tickers (list): List of stock ticker symbols (e.g., ['AAPL', 'GOOGL']).
        
    Returns:
        dict: A dictionary where keys are tickers and values contain price history and news.
    """
    stock_data = {}
    
    for ticker in tickers:
        try:
            print(f"Fetching data for {ticker}...")
            stock = yf.Ticker(ticker)
            
            # Get last 5 days of history
            hist = stock.history(period="5d")
            
            # Get recent news (limit to top 3)
            news = stock.news[:3] if stock.news else []
            
            stock_data[ticker] = {
                "history": hist.to_string(),
                "current_price": hist['Close'].iloc[-1] if not hist.empty else "N/A",
                "news": [n['title'] for n in news]
            }
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
            stock_data[ticker] = {"error": str(e)}
            
    return stock_data

if __name__ == "__main__":
    # Test run
    data = get_stock_data(["AAPL", "MSFT"])
    print(data)
