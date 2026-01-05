import pandas as pd
from datetime import datetime

class BudgetTracker:
    """Track government budget allocations and spending"""
    
    def __init__(self):
        self.budget_data = self.load_budget_data()
    
    def load_budget_data(self):
        """Load government budget allocation data"""
        # FY 2024-25 Budget Data (in Crores)
        data = {
            'Sector': [
                'Infrastructure', 'Defense', 'Healthcare', 'Green Energy', 
                'Agriculture', 'Education', 'Digital India', 'Railways',
                'Manufacturing', 'MSME', 'Urban Development', 'Rural Development',
                'Space & Science', 'Tourism', 'Textiles'
            ],
            'Budget_FY24': [127000, 111000, 77000, 55000, 110000, 62000, 36000, 81000, 68000, 48000, 45000, 95000, 28000, 12000, 18000],
            'Budget_FY25': [150000, 125000, 89000, 75000, 120000, 68000, 45000, 95000, 82000, 55000, 52000, 102000, 32000, 15000, 20000],
            'Key_Schemes': [
                'PM Gati Shakti, Bharatmala',
                'Atmanirbhar Bharat, Make in India',
                'Ayushman Bharat, PM-JAY',
                'National Green Hydrogen Mission, PLI Solar',
                'PM-KISAN, MSP Support',
                'NEP 2020, Digital Education',
                'Digital India 2.0, BharatNet',
                'Vande Bharat, Station Modernization',
                'PLI Schemes, Production Linked',
                'MUDRA, Stand Up India',
                'Smart Cities, AMRUT',
                'MGNREGA, PM Awas Yojana',
                'Gaganyaan, Chandrayaan',
                'Swadesh Darshan, PRASHAD',
                'PM MITRA, Technical Textiles'
            ],
            'Top_Stocks': [
                'L&T, IRB Infra, Ashoka Buildcon',
                'HAL, BEL, Mazagon Dock',
                'Apollo Hospitals, Dr Reddy, Sun Pharma',
                'Adani Green, Tata Power, Waaree',
                'UPL, Coromandel, PI Industries',
                'NIIT, Aptech, Zee Learn',
                'TCS, Infosys, HCL Tech',
                'IRCTC, RVNL, IRFC',
                'Tata Motors, Bharat Forge, Dixon',
                'Bajaj Finance, HDFC Bank, AU Bank',
                'DLF, Oberoi Realty, Prestige',
                'Jain Irrigation, Escorts, VST',
                'ISRO suppliers, Centum Electronics',
                'Indian Hotels, Lemon Tree, Thomas Cook',
                'Welspun, Trident, Vardhman'
            ]
        }
        
        df = pd.DataFrame(data)
        df['YoY_Change_%'] = ((df['Budget_FY25'] - df['Budget_FY24']) / df['Budget_FY24'] * 100).round(2)
        df['Priority'] = df['YoY_Change_%'].apply(self._get_priority)
        
        return df
    
    def _get_priority(self, change):
        """Determine priority based on budget change"""
        if change >= 25:
            return 'Very High'
        elif change >= 15:
            return 'High'
        elif change >= 5:
            return 'Medium'
        else:
            return 'Low'
    
    def get_top_sectors(self, n=5):
        """Get top N sectors by budget allocation"""
        return self.budget_data.nlargest(n, 'Budget_FY25')
    
    def get_high_growth_sectors(self, threshold=15):
        """Get sectors with high YoY growth"""
        return self.budget_data[self.budget_data['YoY_Change_%'] >= threshold]
    
    def get_sector_details(self, sector_name):
        """Get detailed info for a specific sector"""
        return self.budget_data[self.budget_data['Sector'] == sector_name]
    
    def get_investment_recommendations(self):
        """Generate investment recommendations based on budget"""
        high_priority = self.budget_data[self.budget_data['Priority'].isin(['Very High', 'High'])]
        
        recommendations = []
        for _, row in high_priority.iterrows():
            recommendations.append({
                'Sector': row['Sector'],
                'Budget': f"₹{row['Budget_FY25']:,} Cr",
                'Growth': f"{row['YoY_Change_%']}%",
                'Stocks': row['Top_Stocks'],
                'Schemes': row['Key_Schemes']
            })
        
        return recommendations

# Policy Impact Tracker
class PolicyTracker:
    """Track policy changes and their market impact"""
    
    @staticmethod
    def get_recent_policies():
        """Get recent policy announcements"""
        policies = [
            {
                'date': '2024-02-01',
                'policy': 'PLI Scheme for Electronics Manufacturing',
                'allocation': '₹55,000 Cr',
                'sectors': ['Electronics', 'Manufacturing'],
                'impact': 'Very Positive',
                'stocks': 'Dixon, Amber, Kaynes Technology'
            },
            {
                'date': '2024-01-15',
                'policy': 'National Green Hydrogen Mission',
                'allocation': '₹19,744 Cr',
                'sectors': ['Green Energy', 'Chemicals'],
                'impact': 'Very Positive',
                'stocks': 'Reliance, Adani Green, NTPC'
            },
            {
                'date': '2024-01-10',
                'policy': 'Digital India 2.0',
                'allocation': '₹45,000 Cr',
                'sectors': ['IT', 'Telecom'],
                'impact': 'Positive',
                'stocks': 'TCS, Infosys, Bharti Airtel'
            },
            {
                'date': '2023-12-20',
                'policy': 'Semiconductor Mission',
                'allocation': '₹76,000 Cr',
                'sectors': ['Semiconductors', 'Electronics'],
                'impact': 'Very Positive',
                'stocks': 'Tata Electronics, VEDL, HCL Tech'
            },
            {
                'date': '2023-12-01',
                'policy': 'PM Awas Yojana Extension',
                'allocation': '₹79,000 Cr',
                'sectors': ['Real Estate', 'Cement'],
                'impact': 'Positive',
                'stocks': 'UltraTech, Ambuja, DLF'
            }
        ]
        
        return pd.DataFrame(policies)
