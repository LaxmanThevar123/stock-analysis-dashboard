import pandas as pd
from datetime import datetime

class GlobalImpactAnalyzer:
    """Analyze global events and their impact on Indian stocks"""
    
    def __init__(self):
        self.commodity_map = self.load_commodity_dependencies()
        self.global_events = self.load_recent_events()
    
    def load_commodity_dependencies(self):
        """Map commodities to dependent sectors and substitutes"""
        return {
            'Cobalt': {
                'source_countries': ['Congo (70%)', 'Russia', 'Australia'],
                'dependent_sectors': ['EV Batteries', 'Mobile Manufacturing', 'Electronics'],
                'indian_companies_affected': [
                    'Tata Motors (EV)', 'M&M (EV)', 'Ola Electric',
                    'Dixon Technologies', 'Amber Enterprises'
                ],
                'substitutes': {
                    'Lithium Iron Phosphate (LFP)': ['CATL suppliers', 'Reliance (planned)'],
                    'Sodium-ion batteries': ['Reliance New Energy', 'ISRO tech'],
                    'Nickel-based batteries': ['Hindalco', 'Vedanta']
                },
                'impact': 'High',
                'price_trend': '+42% (supply disruption)'
            },
            'Lithium': {
                'source_countries': ['Australia', 'Chile', 'China'],
                'dependent_sectors': ['EV Batteries', 'Energy Storage', 'Electronics'],
                'indian_companies_affected': [
                    'Tata Motors', 'Ola Electric', 'Exide Industries',
                    'Amara Raja Batteries'
                ],
                'substitutes': {
                    'Sodium-ion': ['Reliance', 'ISRO collaboration'],
                    'Aluminum-ion': ['Research stage'],
                    'Solid-state': ['Tata Motors R&D']
                },
                'impact': 'Very High',
                'price_trend': '+52% (demand surge)'
            },
            'Rare Earth Elements': {
                'source_countries': ['China (80%)', 'USA', 'Australia'],
                'dependent_sectors': ['Electronics', 'Defense', 'Renewable Energy'],
                'indian_companies_affected': [
                    'HAL', 'BEL', 'Tata Power', 'Adani Green'
                ],
                'substitutes': {
                    'Domestic mining': ['IREL India', 'Govt exploration'],
                    'Recycling tech': ['Attero Recycling', 'TES-AMM India']
                },
                'impact': 'High',
                'price_trend': '+35% (geopolitical)'
            },
            'Crude Oil': {
                'source_countries': ['Middle East', 'Russia', 'USA'],
                'dependent_sectors': ['Petrochemicals', 'Transportation', 'Manufacturing'],
                'indian_companies_affected': [
                    'Reliance', 'ONGC', 'BPCL', 'IOC', 'HPCL'
                ],
                'substitutes': {
                    'Green Hydrogen': ['Reliance', 'Adani', 'NTPC'],
                    'Biofuels': ['Indian Oil', 'HPCL'],
                    'Electric mobility': ['Tata Motors', 'Ola Electric']
                },
                'impact': 'Very High',
                'price_trend': '+18% (OPEC cuts)'
            },
            'Semiconductor Chips': {
                'source_countries': ['Taiwan', 'South Korea', 'China'],
                'dependent_sectors': ['Electronics', 'Auto', 'Defense', 'IT Hardware'],
                'indian_companies_affected': [
                    'Dixon', 'Amber', 'Tata Motors', 'M&M', 'HAL'
                ],
                'substitutes': {
                    'Domestic manufacturing': ['Tata Electronics', 'Vedanta-Foxconn'],
                    'Design capabilities': ['HCL Tech', 'Wipro'],
                    'Import diversification': ['Vietnam, Malaysia sourcing']
                },
                'impact': 'Critical',
                'price_trend': '+28% (shortage)'
            }
        }
    
    def load_recent_events(self):
        """Load recent global events affecting supply chains"""
        return [
            {
                'date': '2025-01-15',
                'event': 'Congo Cobalt Export Restrictions Extended',
                'commodity': 'Cobalt',
                'impact_level': 'High',
                'affected_sectors': ['EV', 'Mobile Manufacturing', 'Electronics'],
                'price_impact': '+42%',
                'timeline': '6-12 months',
                'indian_impact': 'EV manufacturers accelerating LFP battery adoption',
                'opportunities': [
                    'LFP battery manufacturers',
                    'Sodium-ion battery research',
                    'Battery recycling companies'
                ]
            },
            {
                'date': '2025-01-20',
                'event': 'China Rare Earth Export Quotas Reduced',
                'commodity': 'Rare Earth Elements',
                'impact_level': 'Very High',
                'affected_sectors': ['Electronics', 'Defense', 'Renewable Energy'],
                'price_impact': '+38%',
                'timeline': '12-24 months',
                'indian_impact': 'Defense and renewable sectors accelerating domestic sourcing',
                'opportunities': [
                    'Domestic rare earth mining (IREL)',
                    'Recycling technologies',
                    'Alternative materials research'
                ]
            },
            {
                'date': '2025-02-01',
                'event': 'OPEC+ Production Cuts Extended',
                'commodity': 'Crude Oil',
                'impact_level': 'High',
                'affected_sectors': ['Petrochemicals', 'Transportation', 'Manufacturing'],
                'price_impact': '+18%',
                'timeline': '3-6 months',
                'indian_impact': 'Accelerated green energy transition, EV adoption surge',
                'opportunities': [
                    'Green hydrogen projects',
                    'EV adoption acceleration',
                    'Renewable energy stocks'
                ]
            },
            {
                'date': '2025-01-10',
                'event': 'Taiwan Semiconductor Capacity Constraints',
                'commodity': 'Semiconductor Chips',
                'impact_level': 'Critical',
                'affected_sectors': ['Electronics', 'Auto', 'IT Hardware'],
                'price_impact': '+28%',
                'timeline': '18-36 months',
                'indian_impact': 'India Semiconductor Mission gaining momentum, local production scaling',
                'opportunities': [
                    'India Semiconductor Mission beneficiaries',
                    'Tata Electronics, Vedanta-Foxconn JV',
                    'Design services (HCL, Wipro)'
                ]
            }
        ]
    
    def analyze_event_impact(self, commodity):
        """Analyze impact of commodity disruption"""
        if commodity not in self.commodity_map:
            return None
        
        data = self.commodity_map[commodity]
        
        return {
            'commodity': commodity,
            'impact_level': data['impact'],
            'price_trend': data['price_trend'],
            'affected_companies': data['indian_companies_affected'],
            'substitute_options': data['substitutes'],
            'dependent_sectors': data['dependent_sectors']
        }
    
    def get_substitute_projections(self, commodity):
        """Get substitute material projections and stock recommendations"""
        if commodity not in self.commodity_map:
            return []
        
        substitutes = self.commodity_map[commodity]['substitutes']
        projections = []
        
        for substitute, companies in substitutes.items():
            projections.append({
                'substitute': substitute,
                'companies': ', '.join(companies),
                'adoption_timeline': self._get_adoption_timeline(substitute),
                'market_potential': self._get_market_potential(substitute),
                'investment_rating': self._get_investment_rating(substitute)
            })
        
        return projections
    
    def _get_adoption_timeline(self, substitute):
        """Estimate adoption timeline"""
        timelines = {
            'Lithium Iron Phosphate (LFP)': '1-2 years (Already in use)',
            'Sodium-ion batteries': '2-3 years (Pilot stage)',
            'Nickel-based batteries': '1-2 years (Established)',
            'Green Hydrogen': '3-5 years (Infrastructure building)',
            'Biofuels': '1-2 years (Scaling up)',
            'Domestic manufacturing': '3-5 years (Under construction)',
            'Solid-state': '5-7 years (R&D stage)'
        }
        return timelines.get(substitute, '2-4 years')
    
    def _get_market_potential(self, substitute):
        """Estimate market potential"""
        potential = {
            'Lithium Iron Phosphate (LFP)': 'Very High',
            'Sodium-ion batteries': 'High',
            'Green Hydrogen': 'Very High',
            'Domestic manufacturing': 'Critical',
            'Biofuels': 'Medium'
        }
        return potential.get(substitute, 'Medium')
    
    def _get_investment_rating(self, substitute):
        """Get investment rating for substitute"""
        ratings = {
            'Lithium Iron Phosphate (LFP)': 'BUY',
            'Sodium-ion batteries': 'ACCUMULATE',
            'Green Hydrogen': 'STRONG BUY',
            'Domestic manufacturing': 'BUY',
            'Nickel-based batteries': 'HOLD',
            'Biofuels': 'ACCUMULATE'
        }
        return ratings.get(substitute, 'HOLD')
    
    def get_supply_chain_risks(self):
        """Identify supply chain vulnerabilities"""
        risks = []
        
        for commodity, data in self.commodity_map.items():
            # Check if heavily dependent on single country
            sources = data['source_countries']
            if any('%' in s and int(s.split('(')[1].split('%')[0]) > 50 for s in sources):
                risks.append({
                    'commodity': commodity,
                    'risk_level': 'High',
                    'reason': f"Over 50% supply from single source",
                    'affected_sectors': ', '.join(data['dependent_sectors']),
                    'mitigation': 'Diversify suppliers, develop substitutes'
                })
        
        return risks
    
    def get_investment_opportunities(self, event_type='all'):
        """Get investment opportunities from global disruptions"""
        opportunities = []
        
        for event in self.global_events:
            for opp in event['opportunities']:
                opportunities.append({
                    'opportunity': opp,
                    'trigger_event': event['event'],
                    'timeline': event['timeline'],
                    'impact_level': event['impact_level'],
                    'commodity': event['commodity']
                })
        
        return opportunities

class SupplyChainMonitor:
    """Monitor global supply chain disruptions"""
    
    @staticmethod
    def get_critical_alerts():
        """Get critical supply chain alerts"""
        return [
            {
                'alert': '🚨 Cobalt prices up 42% - Congo export restrictions extended (FY26)',
                'action': 'BUY: LFP battery makers, SELL: Cobalt-dependent EV stocks',
                'stocks': 'BUY: Reliance (LFP scaling), Exide | AVOID: High cobalt dependency stocks'
            },
            {
                'alert': '⚠️ Rare earth shortage intensifies - China quotas reduced (FY26)',
                'action': 'BUY: Domestic mining, recycling tech',
                'stocks': 'BUY: IREL India, Attero Recycling'
            },
            {
                'alert': '📈 Semiconductor shortage persists - Taiwan capacity constraints (FY26)',
                'action': 'BUY: India Semiconductor Mission beneficiaries',
                'stocks': 'BUY: Tata Electronics, HCL Tech (design), Dixon (assembly)'
            },
            {
                'alert': '⚡ Oil prices surge 18% - OPEC+ cuts extended (FY26)',
                'action': 'BUY: Green energy, EV stocks | SELL: High fuel cost airlines',
                'stocks': 'BUY: Adani Green, Tata Power, Ola Electric'
            }
        ]
    
    @staticmethod
    def get_geopolitical_risks():
        """Track geopolitical risks affecting supply"""
        return pd.DataFrame({
            'Region': ['Congo', 'China', 'Taiwan', 'Middle East', 'Russia'],
            'Commodity': ['Cobalt', 'Rare Earth', 'Semiconductors', 'Crude Oil', 'Palladium'],
            'Risk_Level': ['High', 'Very High', 'Critical', 'Medium', 'High'],
            'India_Dependency': ['Medium', 'High', 'Very High', 'High', 'Low'],
            'Mitigation_Status': ['In Progress', 'Planned', 'Active', 'Diversifying', 'Completed']
        })
