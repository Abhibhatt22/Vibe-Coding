import streamlit as st
import pandas as pd
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Agentic Campaign Optimizer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    
    .underperformer {
        background-color: #ffebee;
        border-left: 4px solid #d32f2f;
    }
    
    .good-performer {
        background-color: #e8f5e9;
        border-left: 4px solid #388e3c;
    }
    
    h1 {
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    
    h2 {
        color: #1f77b4;
        margin-top: 2rem;
    }
    
    .stMetric {
        background-color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize Streamlit session state variables."""
    if 'data_loaded' not in st.session_state:
        st.session_state.data_loaded = False
    
    if 'df' not in st.session_state:
        st.session_state.df = None
    
    if 'agent_response' not in st.session_state:
        st.session_state.agent_response = None
    
    if 'selected_segment' not in st.session_state:
        st.session_state.selected_segment = None


def load_marketing_data():
    """Load marketing data from CSV file."""
    csv_path = 'data/marketing_campaigns.csv'
    
    if not os.path.exists(csv_path):
        st.warning("📊 Data file not found. Generating fresh data...")
        
        # Import and run data generator
        from utils.data_generator import generate_marketing_data, save_data_to_files
        
        df = generate_marketing_data(n_rows=500)
        save_data_to_files(df, output_dir='data')
        st.success("✅ Data generated and saved!")
        return df
    
    return pd.read_csv(csv_path)


# Initialize session state
initialize_session_state()

# Load data
if not st.session_state.data_loaded:
    st.session_state.df = load_marketing_data()
    st.session_state.data_loaded = True

df = st.session_state.df

# Main app structure
st.title("🤖 Agentic Campaign Optimization Engine")

st.markdown("""
---
### 🎯 Workshop Overview

Welcome to the **Agentic Campaign Optimization Engine** — an interactive demonstration of how AI agents 
can autonomously analyze marketing performance, identify problems, and recommend solutions.

**In this workshop, you'll explore:**
1. **Campaign Dashboard** — Monitor your marketing performance across platforms and segments
2. **Anomaly Detection** — Identify underperforming segments automatically
3. **Creative Optimization** — Let an AI agent rewrite your ad copy for failing campaigns
4. **Budget Reallocation** — See how AI would reallocate your budget for maximum ROI

This is not a replacement for human judgment—it's a **decision support system** that amplifies your marketing team's capabilities.

---
""")

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio(
    "Select a page:",
    ["Dashboard", "Anomaly Detection", "Creative Optimization", "Budget Reallocation"],
    index=0
)

# Load the appropriate page
if page == "Dashboard":
    from pages import dashboard_page
    dashboard_page.render(df)

elif page == "Anomaly Detection":
    from pages import anomaly_page
    anomaly_page.render(df)

elif page == "Creative Optimization":
    from pages import creative_optimization_page
    creative_optimization_page.render(df, st)

elif page == "Budget Reallocation":
    from pages import budget_reallocation_page
    budget_reallocation_page.render(df)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📚 About This App

**Agentic Campaign Optimizer v1.0**

Built with ❤️ for marketing automation workshops.

[GitHub](https://github.com) • [Docs](https://example.com)
""")

# Data info
with st.sidebar.expander("📊 Data Info"):
    st.write(f"**Total Records:** {len(df):,}")
    st.write(f"**Total Spend:** ${df['Spend'].sum():,.2f}")
    st.write(f"**Total Conversions:** {df['Conversions'].sum():,}")
    st.write(f"**Date Generated:** 2024")
    
    # Segments
    st.write("\n**Audience Segments:**")
    for segment in df['Audience_Segment'].unique():
        st.write(f"• {segment}")
