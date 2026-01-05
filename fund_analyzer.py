import pandas as pd
import streamlit as st
import plotly.express as px

def get_top_equity_funds():
    """Returns top performing equity funds data"""
    funds_data = {
        'Fund Name': [
            'Axis Bluechip Fund', 'Mirae Asset Large Cap', 'ICICI Pru Bluechip',
            'Axis Midcap Fund', 'DSP Midcap Fund', 'Kotak Emerging Equity',
            'Axis Small Cap Fund', 'SBI Small Cap Fund', 'Nippon Small Cap',
            'ICICI Pru Technology', 'SBI Healthcare Opp', 'Mirae Infrastructure'
        ],
        'Category': [
            'Large Cap', 'Large Cap', 'Large Cap',
            'Mid Cap', 'Mid Cap', 'Mid Cap', 
            'Small Cap', 'Small Cap', 'Small Cap',
            'Sectoral', 'Sectoral', 'Sectoral'
        ],
        '1Y Return (%)': [12.5, 14.2, 11.8, 19.3, 17.6, 18.9, 22.1, 20.4, 21.7, 16.8, 15.2, 18.3],
        '3Y Return (%)': [13.8, 15.1, 12.9, 18.7, 16.9, 19.2, 21.3, 19.8, 20.6, 17.4, 14.8, 17.9],
        'Risk Level': [
            'Low', 'Low', 'Low',
            'Medium', 'Medium', 'Medium',
            'High', 'High', 'High', 
            'Medium', 'Medium', 'High'
        ],
        'Min Investment': [500, 1000, 1000, 500, 1000, 1000, 500, 1000, 1000, 500, 1000, 1000]
    }
    return pd.DataFrame(funds_data)

def display_fund_analysis():
    """Display fund analysis in Streamlit"""
    st.header("🏆 Top Equity Funds Analysis")
    
    df = get_top_equity_funds()
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        category_filter = st.selectbox("Category", ['All'] + list(df['Category'].unique()))
    with col2:
        risk_filter = st.selectbox("Risk Level", ['All'] + list(df['Risk Level'].unique()))
    
    # Apply filters
    filtered_df = df.copy()
    if category_filter != 'All':
        filtered_df = filtered_df[filtered_df['Category'] == category_filter]
    if risk_filter != 'All':
        filtered_df = filtered_df[filtered_df['Risk Level'] == risk_filter]
    
    # Display table
    st.dataframe(filtered_df, use_container_width=True)
    
    # Returns chart
    fig = px.scatter(filtered_df, x='1Y Return (%)', y='3Y Return (%)', 
                     color='Category', size='Min Investment',
                     hover_data=['Fund Name', 'Risk Level'],
                     title="Fund Returns Comparison")
    st.plotly_chart(fig, use_container_width=True)
    
    # Top picks by category
    st.subheader("📈 Top Picks by Category")
    for category in filtered_df['Category'].unique():
        cat_funds = filtered_df[filtered_df['Category'] == category]
        top_fund = cat_funds.loc[cat_funds['3Y Return (%)'].idxmax()]
        st.write(f"**{category}**: {top_fund['Fund Name']} ({top_fund['3Y Return (%)']}% 3Y return)")

def get_fund_recommendations(budget_sectors):
    """Get fund recommendations based on budget analysis"""
    sector_funds = {
        'Infrastructure': ['Mirae Infrastructure', 'ICICI Pru Infrastructure'],
        'Technology': ['ICICI Pru Technology', 'Franklin India Technology'],
        'Healthcare': ['SBI Healthcare Opp', 'Aditya Birla Healthcare'],
        'Manufacturing': ['Axis Manufacturing Fund', 'DSP Manufacturing'],
        'Energy': ['SBI Energy Opp', 'Invesco India Energy']
    }
    
    recommendations = []
    for sector in budget_sectors:
        if sector in sector_funds:
            recommendations.extend(sector_funds[sector])
    
    return recommendations