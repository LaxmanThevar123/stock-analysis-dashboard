import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

class SectorAnalyzer:
    """Analyze sector performance and fundamentals"""
    
    def __init__(self):
        self.sectors = self._load_sector_data()
    
    def _load_sector_data(self):
        """Load sector indices and stocks"""
        return {
            'IT': {
                'index': '^CNXIT',
                'stocks': ['TCS.NS', 'INFY.NS', 'HCLTECH.NS', 'WIPRO.NS', 'TECHM.NS'],
                'names': ['TCS', 'Infosys', 'HCL Tech', 'Wipro', 'Tech Mahindra']
            },
            'Banking': {
                'index': '^CNXBANK',
                'stocks': ['HDFCBANK.NS', 'ICICIBANK.NS', 'SBIN.NS', 'KOTAKBANK.NS', 'AXISBANK.NS'],
                'names': ['HDFC Bank', 'ICICI Bank', 'SBI', 'Kotak Bank', 'Axis Bank']
            },
            'Auto': {
                'index': '^CNXAUTO',
                'stocks': ['TATAMOTORS.NS', 'M&M.NS', 'MARUTI.NS', 'BAJAJ-AUTO.NS', 'HEROMOTOCO.NS'],
                'names': ['Tata Motors', 'M&M', 'Maruti', 'Bajaj Auto', 'Hero MotoCorp']
            },
            'Pharma': {
                'index': '^CNXPHARMA',
                'stocks': ['SUNPHARMA.NS', 'DRREDDY.NS', 'CIPLA.NS', 'DIVISLAB.NS', 'APOLLOHOSP.NS'],
                'names': ['Sun Pharma', 'Dr Reddy', 'Cipla', 'Divi\'s Lab', 'Apollo Hospitals']
            },
            'Energy': {
                'index': '^CNXENERGY',
                'stocks': ['RELIANCE.NS', 'ONGC.NS', 'BPCL.NS', 'IOC.NS', 'NTPC.NS'],
                'names': ['Reliance', 'ONGC', 'BPCL', 'IOC', 'NTPC']
            },
            'Infrastructure': {
                'index': '^CNXINFRA',
                'stocks': ['LT.NS', 'ADANIPORTS.NS', 'ULTRACEMCO.NS', 'GRASIM.NS', 'AMBUJACEM.NS'],
                'names': ['L&T', 'Adani Ports', 'UltraTech', 'Grasim', 'Ambuja Cement']
            }
        }
    
    def get_sector_performance(self, sector, period='6mo'):
        """Get sector index performance"""
        try:
            sector_data = self.sectors.get(sector)
            if not sector_data:
                return None
            
            index = yf.Ticker(sector_data['index'])
            hist = index.history(period=period)
            
            if hist.empty:
                return None
            
            start_price = hist['Close'].iloc[0]
            end_price = hist['Close'].iloc[-1]
            returns = ((end_price - start_price) / start_price) * 100
            
            return {
                'sector': sector,
                'returns': round(returns, 2),
                'current_price': round(end_price, 2),
                'high': round(hist['High'].max(), 2),
                'low': round(hist['Low'].min(), 2)
            }
        except:
            return None
    
    def get_top_stocks_in_sector(self, sector, metric='returns'):
        """Get top performing stocks in a sector"""
        sector_data = self.sectors.get(sector)
        if not sector_data:
            return []
        
        stocks_performance = []
        for ticker, name in zip(sector_data['stocks'], sector_data['names']):
            try:
                stock = yf.Ticker(ticker)
                hist = stock.history(period='6mo')
                info = stock.info
                
                if not hist.empty:
                    returns = ((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0]) * 100
                    
                    stocks_performance.append({
                        'name': name,
                        'ticker': ticker,
                        'returns': round(returns, 2),
                        'pe_ratio': info.get('trailingPE', 'N/A'),
                        'market_cap': info.get('marketCap', 0) / 10000000,  # In Crores
                        'current_price': round(hist['Close'].iloc[-1], 2)
                    })
            except:
                continue
        
        return sorted(stocks_performance, key=lambda x: x['returns'], reverse=True)
    
    def compare_sectors(self, period='6mo'):
        """Compare performance across all sectors"""
        comparison = []
        
        for sector in self.sectors.keys():
            perf = self.get_sector_performance(sector, period)
            if perf:
                comparison.append(perf)
        
        return sorted(comparison, key=lambda x: x['returns'], reverse=True)
    
    def get_sector_fundamentals(self, sector):
        """Get average fundamentals for sector"""
        sector_data = self.sectors.get(sector)
        if not sector_data:
            return None
        
        pe_ratios = []
        pb_ratios = []
        roe_values = []
        
        for ticker in sector_data['stocks']:
            try:
                stock = yf.Ticker(ticker)
                info = stock.info
                
                if 'trailingPE' in info and info['trailingPE']:
                    pe_ratios.append(info['trailingPE'])
                if 'priceToBook' in info and info['priceToBook']:
                    pb_ratios.append(info['priceToBook'])
                if 'returnOnEquity' in info and info['returnOnEquity']:
                    roe_values.append(info['returnOnEquity'] * 100)
            except:
                continue
        
        return {
            'sector': sector,
            'avg_pe': round(sum(pe_ratios) / len(pe_ratios), 2) if pe_ratios else 'N/A',
            'avg_pb': round(sum(pb_ratios) / len(pb_ratios), 2) if pb_ratios else 'N/A',
            'avg_roe': round(sum(roe_values) / len(roe_values), 2) if roe_values else 'N/A'
        }

class MacroEconomicData:
    """Fetch macro economic indicators"""
    
    @staticmethod
    def get_indicators():
        """Get current macro indicators (mock data - integrate with real APIs)"""
        return {
            'gdp_growth': 7.2,
            'inflation_cpi': 5.1,
            'repo_rate': 6.5,
            'usd_inr': 83.2,
            'crude_oil': 82.5,
            'gold_price': 62500,
            'fii_inflow': 15000,  # Crores
            'dii_inflow': 18000   # Crores
        }
    
    @staticmethod
    def get_gdp_trend():
        """Get GDP growth trend"""
        return pd.DataFrame({
            'Quarter': ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024'],
            'GDP_Growth': [6.1, 6.3, 7.6, 8.4, 7.2]
        })
    
    @staticmethod
    def get_inflation_trend():
        """Get inflation trend"""
        return pd.DataFrame({
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'CPI': [5.7, 5.9, 4.9, 4.8, 4.7, 5.1]
        })
