import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import requests
import json
import os
from global_impact_analyzer import GlobalImpactAnalyzer, SupplyChainMonitor
from fund_analyzer import display_fund_analysis, get_fund_recommendations

# Access control check
if os.getenv("APP_ACCESS_ENABLED", "false").lower() != "true":
    st.error("🚫 Access Restricted")
    st.info("This application is currently not accessible. Please contact the administrator.")
    st.stop()

st.set_page_config(page_title="Top-Down Stock Analysis", page_icon="📊", layout="wide")

# Sidebar
st.sidebar.title("🔍 Top-Down Analysis")
analysis_mode = st.sidebar.radio("Select Analysis Level", 
    ["📈 Macro Economy", "🏭 Sector Analysis", "🏢 Company Analysis", "📰 News & Budget", "🌍 Global Impact", "💰 Fund Analysis"])

# Main Title
st.title("📊 Top-Down Stock Analysis Dashboard")
st.markdown("---")

# ===== MACRO ECONOMY =====
if analysis_mode == "📈 Macro Economy":
    st.header("📈 Macro Economic Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("GDP Growth", "7.8%", "0.6%")
    with col2:
        st.metric("Inflation (CPI)", "4.8%", "-0.3%")
    with col3:
        st.metric("Interest Rate", "6.5%", "0%")
    with col4:
        st.metric("USD/INR", "₹82.8", "-0.4")
    
    st.markdown("---")
    
    # Economic Indicators Chart
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("GDP Growth Trend")
        gdp_data = pd.DataFrame({
            'Quarter': ['Q1 2025', 'Q2 2025', 'Q3 2025', 'Q4 2025', 'Q1 2026'],
            'GDP Growth %': [7.2, 7.8, 8.1, 7.9, 7.6]
        })
        fig = px.line(gdp_data, x='Quarter', y='GDP Growth %', markers=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Inflation Trend")
        inflation_data = pd.DataFrame({
            'Month': ['Aug 25', 'Sep 25', 'Oct 25', 'Nov 25', 'Dec 25', 'Jan 26'],
            'CPI %': [5.2, 4.9, 4.6, 4.5, 4.3, 4.8]
        })
        fig = px.bar(inflation_data, x='Month', y='CPI %', color='CPI %')
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("🎯 Investment Recommendation")
    st.success("✅ **Bullish Market**: Strong GDP growth with controlled inflation. Favor cyclical sectors.")

# ===== SECTOR ANALYSIS =====
elif analysis_mode == "🏭 Sector Analysis":
    st.header("🏭 Sector Performance & Government Spending")
    
    # Government Budget Allocation
    st.subheader("💰 Government Budget Allocation (FY 2025-26)")
    
    budget_data = pd.DataFrame({
        'Sector': ['Infrastructure', 'Defense', 'Healthcare', 'Green Energy', 'Agriculture', 
                   'Education', 'Digital India', 'Railways', 'Manufacturing', 'MSME'],
        'Budget (₹ Cr)': [175000, 140000, 105000, 95000, 135000, 78000, 58000, 110000, 98000, 65000],
        'YoY Change %': [17, 12, 18, 27, 12, 15, 29, 16, 20, 18]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(budget_data.sort_values('Budget (₹ Cr)', ascending=False).head(10), 
                     x='Sector', y='Budget (₹ Cr)', color='YoY Change %',
                     title="Top 10 Sectors by Budget Allocation")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.pie(budget_data, values='Budget (₹ Cr)', names='Sector', 
                     title="Budget Distribution")
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Sector Performance
    st.subheader("📊 Sector Performance (Last 6 Months)")
    
    sector_performance = pd.DataFrame({
        'Sector': ['IT', 'Banking', 'Pharma', 'Auto', 'Infrastructure', 'FMCG', 'Energy', 'Metals'],
        'Returns %': [12.5, 18.3, 8.7, 22.1, 28.5, 6.2, 15.8, 19.4],
        'PE Ratio': [25.3, 18.5, 28.9, 22.1, 35.2, 45.6, 12.3, 8.7],
        'Govt Focus': ['High', 'Medium', 'High', 'High', 'Very High', 'Low', 'Very High', 'Medium']
    })
    
    st.dataframe(sector_performance.style.background_gradient(subset=['Returns %'], cmap='RdYlGn'), 
                 use_container_width=True)
    
    # Sector Heatmap
    st.subheader("🔥 Sector Heatmap (Government Focus vs Returns)")
    fig = px.scatter(sector_performance, x='PE Ratio', y='Returns %', 
                     size='Returns %', color='Govt Focus', hover_name='Sector',
                     size_max=60, color_discrete_map={
                         'Very High': 'green', 'High': 'lightgreen', 
                         'Medium': 'yellow', 'Low': 'orange'
                     })
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.subheader("🎯 Top Sectors to Watch")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**🏗️ Infrastructure**\n\n₹1.75L Cr Budget (+17%)\n\nTop Pick: L&T, IRB Infra")
    with col2:
        st.success("**⚡ Green Energy**\n\n₹95K Cr Budget (+27%)\n\nTop Pick: Adani Green, Tata Power")
    with col3:
        st.warning("**🚗 Auto & EV**\n\n24.5% Returns\n\nTop Pick: Tata Motors, M&M")

# ===== COMPANY ANALYSIS =====
elif analysis_mode == "🏢 Company Analysis":
    st.header("🏢 Company Fundamental Analysis")
    
    # Company Selector
    sector = st.selectbox("Select Sector", 
        ['IT', 'Banking', 'Pharma', 'Auto', 'Infrastructure', 'Energy'])
    
    # Sector-specific companies
    sector_companies = {
        'IT': ['TCS', 'Infosys', 'HCL Tech', 'Wipro'],
        'Banking': ['HDFC Bank', 'ICICI Bank', 'SBI', 'Axis Bank'],
        'Pharma': ['Sun Pharma', 'Dr Reddy', 'Cipla', 'Lupin'],
        'Auto': ['Tata Motors', 'M&M', 'Maruti Suzuki', 'Bajaj Auto'],
        'Infrastructure': ['L&T', 'UltraTech', 'Adani Ports', 'IRB Infra'],
        'Energy': ['Reliance Industries', 'ONGC', 'Adani Green', 'Tata Power']
    }
    
    company = st.selectbox("Select Company", sector_companies[sector])
    
    # Sector-specific metrics
    sector_metrics = {
        'IT': {'market_cap': '₹12.5L Cr', 'pe': '24.8', 'roe': '22.1%', 'de': '0.15', 'div': '2.8%'},
        'Banking': {'market_cap': '₹8.9L Cr', 'pe': '16.5', 'roe': '15.8%', 'de': '2.1', 'div': '3.2%'},
        'Pharma': {'market_cap': '₹6.2L Cr', 'pe': '28.9', 'roe': '18.5%', 'de': '0.25', 'div': '1.5%'},
        'Auto': {'market_cap': '₹4.8L Cr', 'pe': '22.1', 'roe': '16.2%', 'de': '0.65', 'div': '2.1%'},
        'Infrastructure': {'market_cap': '₹16.8L Cr', 'pe': '26.2', 'roe': '19.5%', 'de': '0.38', 'div': '2.1%'},
        'Energy': {'market_cap': '₹18.5L Cr', 'pe': '15.8', 'roe': '14.2%', 'de': '0.42', 'div': '0.8%'}
    }
    
    st.markdown("---")
    
    # Company Metrics
    metrics = sector_metrics[sector]
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Market Cap", metrics['market_cap'])
    with col2:
        st.metric("P/E Ratio", metrics['pe'], "-2.3")
    with col3:
        st.metric("ROE", metrics['roe'], "1.3%")
    with col4:
        st.metric("Debt/Equity", metrics['de'], "-0.07")
    with col5:
        st.metric("Dividend Yield", metrics['div'])
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Revenue & Profit Trend")
        financial_data = pd.DataFrame({
            'Year': ['FY21', 'FY22', 'FY23', 'FY24', 'FY25'],
            'Revenue (₹ Cr)': [48000, 52000, 58000, 65000, 72000],
            'Net Profit (₹ Cr)': [8500, 9200, 10500, 12000, 14000]
        })
        fig = go.Figure()
        fig.add_trace(go.Bar(x=financial_data['Year'], y=financial_data['Revenue (₹ Cr)'], 
                             name='Revenue', marker_color='lightblue'))
        fig.add_trace(go.Scatter(x=financial_data['Year'], y=financial_data['Net Profit (₹ Cr)'], 
                                 name='Net Profit', mode='lines+markers', marker_color='green'))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📊 Key Ratios")
        ratios = pd.DataFrame({
            'Metric': ['Current Ratio', 'Quick Ratio', 'Operating Margin', 'Net Margin', 'Asset Turnover'],
            'Value': [1.8, 1.5, '22%', '18%', 1.2],
            'Industry Avg': [1.5, 1.2, '18%', '15%', 1.0],
            'Status': ['✅ Good', '✅ Good', '✅ Above Avg', '✅ Above Avg', '✅ Good']
        })
        st.dataframe(ratios, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Valuation
    st.subheader("💰 Valuation Analysis")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Price", "₹2,680")
    with col2:
        st.metric("Target Price", "₹3,150", "17.5%")
    with col3:
        st.metric("Analyst Rating", "BUY", "Strong")
    
    st.success("✅ **Recommendation**: BUY - Strong fundamentals, government sector focus, undervalued compared to peers")

# ===== NEWS & BUDGET =====
elif analysis_mode == "📰 News & Budget":
    st.header("📰 Latest News & Budget Updates")
    
    # News Feed
    st.subheader("🔔 Real-Time Sector News")
    
    news_data = [
        {
            'time': '2 hours ago',
            'sector': 'Infrastructure',
            'headline': 'Government announces ₹50,000 Cr additional allocation for highway projects (FY 2025-26)',
            'impact': 'Positive',
            'stocks': 'L&T, IRB Infra, Ashoka Buildcon'
        },
        {
            'time': '5 hours ago',
            'sector': 'Green Energy',
            'headline': 'New PLI scheme for solar manufacturing with ₹24,000 Cr outlay (FY 2025-26)',
            'impact': 'Very Positive',
            'stocks': 'Adani Green, Tata Power, Waaree Energies'
        },
        {
            'time': '1 day ago',
            'sector': 'Defense',
            'headline': 'Defense Ministry clears procurement worth ₹70,000 Cr for FY 2025-26',
            'impact': 'Positive',
            'stocks': 'HAL, BEL, Mazagon Dock'
        },
        {
            'time': '1 day ago',
            'sector': 'Banking',
            'headline': 'RBI maintains repo rate at 6.5% for FY 2025-26, signals pause in rate hikes',
            'impact': 'Neutral',
            'stocks': 'HDFC Bank, ICICI Bank, SBI'
        },
        {
            'time': '2 days ago',
            'sector': 'Auto',
            'headline': 'EV subsidy extended for FY 2025-26, ₹10,000 Cr allocated',
            'impact': 'Positive',
            'stocks': 'Tata Motors, M&M, Ola Electric'
        }
    ]
    
    for news in news_data:
        impact_color = 'green' if 'Positive' in news['impact'] else 'orange'
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{news['headline']}**")
                st.caption(f"🏷️ {news['sector']} | ⏰ {news['time']} | 📈 Stocks: {news['stocks']}")
            with col2:
                if 'Very Positive' in news['impact']:
                    st.success(news['impact'])
                elif 'Positive' in news['impact']:
                    st.info(news['impact'])
                else:
                    st.warning(news['impact'])
            st.markdown("---")
    
    # Budget Tracker
    st.subheader("💼 Budget Tracker & Policy Updates")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📅 Upcoming Events")
        events = pd.DataFrame({
            'Date': ['1 Feb 2026', '15 Feb 2026', '28 Feb 2026', '5 Mar 2026'],
            'Event': ['Union Budget 2026-27', 'RBI Monetary Policy', 'Q4 FY26 GDP Data', 'State Budget - Maharashtra FY26'],
            'Impact': ['High', 'High', 'Medium', 'Medium']
        })
        st.dataframe(events, use_container_width=True, hide_index=True)
    
    with col2:
        st.markdown("### 🎯 Key Policy Changes")
        policies = pd.DataFrame({
            'Policy': ['PLI for Electronics 3.0', 'Green Hydrogen Mission', 'Digital India 3.0', 'Atmanirbhar Bharat 4.0'],
            'Allocation': ['₹85K Cr', '₹42K Cr', '₹75K Cr', '₹1.5L Cr'],
            'Status': ['Active FY26', 'Active FY26', 'Active FY26', 'Active FY26']
        })
        st.dataframe(policies, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Sector Alerts
    st.subheader("🚨 Sector Alerts Based on Government Actions")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.error("⚠️ **FMCG Sector**\n\nRising input costs, no new subsidies announced")
    with col2:
        st.success("✅ **Infrastructure**\n\nMassive capex push, 18% budget increase")
    with col3:
        st.info("ℹ️ **IT Sector**\n\nDigital India 2.0 approved, ₹45K Cr allocation")

# ===== GLOBAL IMPACT =====
elif analysis_mode == "🌍 Global Impact":
    st.header("🌍 Global Events & Supply Chain Impact")
    
    analyzer = GlobalImpactAnalyzer()
    monitor = SupplyChainMonitor()
    
    # Critical Alerts
    st.subheader("🚨 Critical Supply Chain Alerts")
    alerts = monitor.get_critical_alerts()
    
    for alert in alerts:
        with st.container():
            col1, col2 = st.columns([2, 1])
            with col1:
                st.warning(alert['alert'])
                st.caption(f"**Action**: {alert['action']}")
            with col2:
                st.info(f"**Stocks**: {alert['stocks']}")
            st.markdown("---")
    
    # Recent Global Events
    st.subheader("📰 Recent Global Events Affecting India")
    
    events_df = pd.DataFrame(analyzer.global_events)
    
    for _, event in events_df.iterrows():
        with st.expander(f"🔴 {event['event']} - {event['date']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Impact Level", event['impact_level'])
            with col2:
                st.metric("Price Impact", event['price_impact'])
            with col3:
                st.metric("Timeline", event['timeline'])
            
            st.markdown(f"**Commodity**: {event['commodity']}")
            st.markdown(f"**Affected Sectors**: {', '.join(event['affected_sectors'])}")
            st.markdown(f"**Indian Impact**: {event['indian_impact']}")
            
            st.markdown("**💡 Investment Opportunities:**")
            for opp in event['opportunities']:
                st.success(f"✅ {opp}")
    
    st.markdown("---")
    
    # Commodity Analysis
    st.subheader("⚙️ Commodity Disruption Analysis")
    
    commodity = st.selectbox("Select Commodity", 
        ['Cobalt', 'Lithium', 'Rare Earth Elements', 'Crude Oil', 'Semiconductor Chips'])
    
    impact = analyzer.analyze_event_impact(commodity)
    
    if impact:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Impact Level", impact['impact_level'])
        with col2:
            st.metric("Price Trend", impact['price_trend'])
        with col3:
            st.metric("Affected Sectors", len(impact['dependent_sectors']))
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🏭 Affected Indian Companies")
            for company in impact['affected_companies']:
                st.markdown(f"- {company}")
        
        with col2:
            st.markdown("### 🔄 Substitute Materials & Companies")
            for substitute, companies in impact['substitute_options'].items():
                st.markdown(f"**{substitute}**")
                st.caption(f"Companies: {', '.join(companies)}")
    
    st.markdown("---")
    
    # Substitute Projections
    st.subheader("📊 Substitute Material Projections")
    
    projections = analyzer.get_substitute_projections(commodity)
    
    if projections:
        proj_df = pd.DataFrame(projections)
        
        # Color code by investment rating
        def color_rating(val):
            colors = {
                'STRONG BUY': 'background-color: darkgreen; color: white',
                'BUY': 'background-color: lightgreen',
                'ACCUMULATE': 'background-color: lightyellow',
                'HOLD': 'background-color: lightgray'
            }
            return colors.get(val, '')
        
        styled_df = proj_df.style.applymap(color_rating, subset=['investment_rating'])
        st.dataframe(styled_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Geopolitical Risks
    st.subheader("🗺️ Geopolitical Supply Chain Risks")
    
    risks_df = monitor.get_geopolitical_risks()
    
    fig = px.scatter(risks_df, x='India_Dependency', y='Risk_Level', 
                     size=[100]*len(risks_df), color='Commodity',
                     hover_name='Region', size_max=60,
                     title='Supply Chain Risk Matrix')
    st.plotly_chart(fig, use_container_width=True)
    
    st.dataframe(risks_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Investment Opportunities
    st.subheader("💰 Investment Opportunities from Global Disruptions")
    
    opportunities = analyzer.get_investment_opportunities()
    opp_df = pd.DataFrame(opportunities)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🚀 High Priority")
        high_priority = opp_df[opp_df['impact_level'] == 'Very High']
        for _, opp in high_priority.iterrows():
            st.success(f"**{opp['opportunity']}**\n\n{opp['trigger_event']}\n\nTimeline: {opp['timeline']}")
    
    with col2:
        st.markdown("### ⚡ Medium Priority")
        med_priority = opp_df[opp_df['impact_level'] == 'High']
        for _, opp in med_priority.iterrows():
            st.info(f"**{opp['opportunity']}**\n\n{opp['trigger_event']}\n\nTimeline: {opp['timeline']}")
    
    with col3:
        st.markdown("### 📌 Watch List")
        low_priority = opp_df[opp_df['impact_level'] == 'Critical']
        for _, opp in low_priority.iterrows():
            st.warning(f"**{opp['opportunity']}**\n\n{opp['trigger_event']}\n\nTimeline: {opp['timeline']}")
    
    st.markdown("---")
    
    # Supply Chain Vulnerabilities
    st.subheader("⚠️ Supply Chain Vulnerabilities")
    
    vulnerabilities = analyzer.get_supply_chain_risks()
    vuln_df = pd.DataFrame(vulnerabilities)
    
    st.dataframe(vuln_df, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Actionable Insights
    st.subheader("🎯 Actionable Investment Strategy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✅ BUY Recommendations")
        st.success("""
        **Based on Global Disruptions:**
        
        1. **LFP Battery Makers** - Cobalt shortage
           - Reliance New Energy, Exide Industries
        
        2. **Green Hydrogen** - Oil price surge
           - Reliance, Adani Green, NTPC
        
        3. **Semiconductor Ecosystem** - Chip shortage
           - Tata Electronics, HCL Tech, Dixon
        
        4. **Domestic Mining** - Rare earth curbs
           - IREL India, Coal India (diversification)
        
        5. **Battery Recycling** - Resource scarcity
           - Attero Recycling, Gravita India
        """)
    
    with col2:
        st.markdown("### ⚠️ AVOID/REDUCE")
        st.error("""
        **High Risk Sectors:**
        
        1. **High Cobalt Dependency EVs**
           - Companies without LFP transition plans
        
        2. **Import-Heavy Electronics**
           - No domestic manufacturing pivot
        
        3. **Fuel-Intensive Airlines**
           - Rising crude oil prices
        
        4. **China-Dependent Supply Chains**
           - Rare earth, semiconductors exposure
        
        5. **Single-Source Commodity Traders**
           - Geopolitical risk concentration
        """)

# ===== FUND ANALYSIS =====
elif analysis_mode == "💰 Fund Analysis":
    display_fund_analysis()
    
    # Integration with budget analysis
    st.markdown("---")
    st.subheader("🎯 Fund Recommendations Based on Budget Analysis")
    
    high_budget_sectors = ['Infrastructure', 'Green Energy', 'Technology', 'Healthcare', 'Manufacturing']
    recommended_funds = get_fund_recommendations(high_budget_sectors)
    
    if recommended_funds:
        st.success(f"**Recommended Funds**: {', '.join(recommended_funds[:3])}")
        st.info("These funds align with high government spending sectors from your budget analysis.")

# Footer
st.markdown("---")
st.caption("📊 Top-Down Analysis Dashboard | Data updated: " + datetime.now().strftime("%Y-%m-%d %H:%M"))
