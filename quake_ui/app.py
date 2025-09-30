import streamlit as st
import requests
import pandas as pd

st.title("🌍 Earth Pulse")

# Fetch data from API
try:
    response = requests.get("http://localhost:8000/alerts?limit=50")
    data = response.json()
    
    if data:
        # Convert to DataFrame for better display
        df = pd.DataFrame(data)
        
        # Show metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Earthquakes", len(df))
        col2.metric("Avg Magnitude", f"{df['magnitude'].mean():.2f}")
        col3.metric("Max Magnitude", f"{df['magnitude'].max():.2f}")
        
        # Show data table
        st.subheader("Recent Earthquakes")
        st.dataframe(df[['place', 'magnitude', 'depth', 'occurred_at']], 
                     use_container_width=True)
    else:
        st.error("No data available")
        
except Exception as e:
    st.error(f"Cannot connect to API. Make sure it's running on port 8000")
    st.error(f"Error: {e}")