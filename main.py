import scraper
import analyzer
import mailer
import config

def main():
    print("--- Stock Analysis AI Agent ---")
    
    # Get inputs
    tickers_input = input("Enter stock tickers (comma-separated, e.g., AAPL, MSFT): ")
    tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]
    
    if not tickers:
        print("No tickers provided. Exiting.")
        return

    recipient_email = input(f"Enter recipient email (default: {config.EMAIL_SENDER}): ")
    if not recipient_email:
        recipient_email = config.EMAIL_SENDER

    # 1. Scrape
    print("\nStep 1: Scraping data...")
    stock_data = scraper.get_stock_data(tickers)
    
    # 2. Analyze
    print("\nStep 2: Analyzing with LLM...")
    report = analyzer.analyze_stock(stock_data)
    
    print("\n--- Analysis Report ---")
    print(report)
    print("-----------------------")

    # 3. Email
    print("\nStep 3: Sending email...")
    mailer.send_email(report, recipient_email)
    
    print("\nDone!")

if __name__ == "__main__":
    main()
