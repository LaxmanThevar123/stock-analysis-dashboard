import requests
from datetime import datetime, timedelta

def get_current_fy_dates():
    """Get current financial year start and end dates (April 1 - March 31)"""
    today = datetime.now()
    if today.month >= 4:  # April onwards = current FY
        fy_start = datetime(today.year, 4, 1)
        fy_end = datetime(today.year + 1, 3, 31)
    else:  # Jan-Mar = previous FY
        fy_start = datetime(today.year - 1, 4, 1)
        fy_end = datetime(today.year, 3, 31)
    return fy_start, fy_end

class NewsAPI:
    """Fetch real-time news for sectors"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key or "YOUR_NEWSAPI_KEY"  # Get free key from newsapi.org
        self.base_url = "https://newsapi.org/v2/everything"
    
    def get_sector_news(self, sector, days=7):
        """Fetch news for specific sector"""
        keywords = {
            'Infrastructure': 'infrastructure OR highway OR construction India',
            'Defense': 'defense OR military procurement India',
            'Green Energy': 'solar OR renewable energy OR green energy India',
            'Banking': 'banking OR RBI OR interest rate India',
            'Auto': 'automobile OR EV OR electric vehicle India',
            'IT': 'IT sector OR software OR technology India',
            'Pharma': 'pharmaceutical OR healthcare India',
            'Agriculture': 'agriculture OR farming India'
        }
        
        query = keywords.get(sector, f"{sector} India")
        fy_start, _ = get_current_fy_dates()
        from_date = fy_start.strftime('%Y-%m-%d')
        
        params = {
            'q': query,
            'from': from_date,
            'sortBy': 'publishedAt',
            'language': 'en',
            'apiKey': self.api_key
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            if response.status_code == 200:
                return response.json().get('articles', [])[:10]
            return []
        except:
            return []
    
    def get_budget_news(self):
        """Fetch government budget related news"""
        params = {
            'q': 'India budget OR government spending OR policy',
            'from': get_current_fy_dates()[0].strftime('%Y-%m-%d'),
            'sortBy': 'publishedAt',
            'language': 'en',
            'apiKey': self.api_key
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            if response.status_code == 200:
                return response.json().get('articles', [])[:15]
            return []
        except:
            return []

# Alternative: Google News RSS (No API key needed)
def get_google_news(sector):
    """Fetch news from Google News RSS"""
    import feedparser
    
    rss_url = f"https://news.google.com/rss/search?q={sector}+India+stock+market&hl=en-IN&gl=IN&ceid=IN:en"
    
    try:
        feed = feedparser.parse(rss_url)
        news = []
        for entry in feed.entries[:10]:
            news.append({
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
                'source': entry.source.title if hasattr(entry, 'source') else 'Google News'
            })
        return news
    except:
        return []
