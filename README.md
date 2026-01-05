# 📊 Top-Down Stock Analysis Dashboard

Complete top-down analysis framework with government budget tracking, sector analysis, and real-time news integration.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Dashboard
```bash
streamlit run app.py
```

### 3. Access Dashboard
Open browser at `http://localhost:8501`

## 📋 Features

### 1. 📈 Macro Economy Analysis
- **Economic Indicators**: GDP, Inflation, Interest Rates, Currency
- **Trend Analysis**: Historical GDP and inflation trends
- **Investment Climate**: Market sentiment based on macro data

### 2. 🏭 Sector Analysis
- **Government Budget Tracking**: Real-time budget allocation by sector
- **Sector Performance**: 6-month returns, PE ratios, fundamentals
- **Budget Heatmap**: Visual representation of govt spending vs returns
- **Top Sectors**: Identify high-growth sectors with government focus

### 3. 🏢 Company Analysis
- **Fundamental Analysis**: P/E, ROE, Debt/Equity, margins
- **Financial Trends**: Revenue and profit growth
- **Valuation**: Target price, analyst ratings
- **Comparative Analysis**: Company vs industry benchmarks

### 4. 📰 News & Budget Updates
- **Real-Time News**: Sector-specific news feed
- **Budget Tracker**: Track government spending and allocations
- **Policy Updates**: Latest policy changes and their impact
- **Sector Alerts**: Automated alerts based on government actions

## 🎯 Top-Down Approach

### Level 1: Macro Economy
- Analyze GDP growth, inflation, interest rates
- Determine overall market sentiment (bullish/bearish)
- Identify favorable economic conditions

### Level 2: Sector Selection
- Review government budget allocations
- Identify sectors with high government spending
- Analyze sector performance and fundamentals
- Select 3-5 high-potential sectors

### Level 3: Company Selection
- Screen companies within selected sectors
- Analyze fundamentals (P/E, ROE, margins)
- Check government policy alignment
- Select top 2-3 stocks per sector

### Level 4: Stock Analysis
- Deep dive into financials
- Valuation analysis
- Entry/exit strategy

## 📊 Government Budget Integration

### Budget Tracking Features:
- **Sector-wise Allocation**: Track ₹ Crores allocated to each sector
- **YoY Growth**: Identify sectors with highest budget increase
- **Key Schemes**: PLI, Green Hydrogen, Digital India, etc.
- **Stock Recommendations**: Top stocks benefiting from govt spending

### High-Priority Sectors (FY 2024-25):
1. **Infrastructure** - ₹1.5L Cr (+18%)
2. **Green Energy** - ₹75K Cr (+35%)
3. **Defense** - ₹1.25L Cr (+12%)
4. **Digital India** - ₹45K Cr (+25%)
5. **Manufacturing** - ₹82K Cr (+20%)

## 📰 News Integration

### News Sources:
- **NewsAPI**: Real-time news (requires API key from newsapi.org)
- **Google News RSS**: Free alternative, no API key needed
- **Sector-Specific**: Filter news by sector

### Setup NewsAPI (Optional):
1. Get free API key from https://newsapi.org
2. Update `news_api.py` with your API key
3. Restart dashboard

## 🔧 Modules

### `app.py`
Main Streamlit dashboard with 4 analysis modes

### `budget_tracker.py`
- Government budget data (FY 2024-25)
- Policy tracker
- Investment recommendations based on budget

### `sector_analyzer.py`
- Sector performance tracking
- Stock fundamentals
- Macro economic indicators

### `news_api.py`
- Real-time news fetching
- Sector-specific news
- Budget news tracking

## 📈 Usage Examples

### Example 1: Find High-Growth Sectors
1. Go to "Sector Analysis"
2. Check "Government Budget Allocation" chart
3. Identify sectors with >20% YoY growth
4. Review sector performance metrics
5. Select top 3 sectors

### Example 2: Stock Selection
1. Select high-growth sector (e.g., Green Energy)
2. Go to "Company Analysis"
3. Compare fundamentals (P/E, ROE, margins)
4. Check government policy alignment
5. Select stocks with strong fundamentals + govt support

### Example 3: Track Budget Impact
1. Go to "News & Budget"
2. Check recent policy announcements
3. Identify sectors with new allocations
4. Review "Sector Alerts"
5. Adjust portfolio accordingly

## 🎨 Customization

### Add New Sectors:
Edit `sector_analyzer.py` and add sector data:
```python
'NewSector': {
    'index': '^CNXNEWSECTOR',
    'stocks': ['STOCK1.NS', 'STOCK2.NS'],
    'names': ['Stock 1', 'Stock 2']
}
```

### Update Budget Data:
Edit `budget_tracker.py` with latest budget figures

### Add News Sources:
Extend `news_api.py` with additional news APIs

## 📊 Data Sources

- **Stock Data**: Yahoo Finance (yfinance)
- **News**: NewsAPI / Google News RSS
- **Budget**: Government of India Budget Portal
- **Economic Data**: RBI, Ministry of Finance

## 🔮 Future Enhancements

- [ ] Live stock price integration
- [ ] Automated portfolio recommendations
- [ ] Email alerts for budget changes
- [ ] PDF report generation
- [ ] Historical budget comparison
- [ ] Sector rotation strategy
- [ ] Risk assessment module

## 📝 Notes

- Budget data is for FY 2024-25 (update annually)
- Stock data is fetched in real-time from Yahoo Finance
- News requires internet connection
- Dashboard works offline with cached data

## 🤝 Support

For issues or questions, refer to module documentation in code comments.

---

**Built with**: Streamlit, Plotly, Pandas, yfinance
**Last Updated**: 2024
