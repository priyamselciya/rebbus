import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Replace with your database details
username = 'root'  # your MySQL username
password = ''  # your MySQL password (empty for default)
host = 'localhost'  # database host
database = 'project_redbus'  # database name
TABLE_NAME = 'busdetail'

# Create a database engine
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')

# Load data from the database
def load_data(engine):
    query = f"SELECT * FROM {TABLE_NAME}"
    df = pd.read_sql(query, engine)
    
    # Convert timedelta to hours and minutes, ensuring the columns are timedelta
    if pd.api.types.is_timedelta64_dtype(df['departing_time']):
        df['departing_time'] = df['departing_time'].apply(lambda x: f"{x.components.hours:02}:{x.components.minutes:02}")
    if pd.api.types.is_timedelta64_dtype(df['reaching_time']):
        df['reaching_time'] = df['reaching_time'].apply(lambda x: f"{x.components.hours:02}:{x.components.minutes:02}")
    
    return df

# Sidebar navigation
def render_sidebar():
    st.sidebar.title("Navigation")
    return st.sidebar.radio("Go to", ["Home", "Data Dashboard"])

# Render Homepage Content
def render_home_page():
    st.title("Exploring Redbus Data with Advanced Scraping and Filtering")
    
    logo_url = "https://s3.rdbuz.com/Images/rdc/rdc-redbus-logo.svg"
    st.image(logo_url, width=300, caption="Redbus Logo", use_column_width=False)
    
    st.markdown("""
        ## Project Overview
        Welcome to the "Redbus Data Scraping and Filtering Project"! This project uses Selenium to automate data extraction from Redbus, including routes, schedules, and availability.
        
        ## Key Business Applications
        - **Travel Aggregators:** Enhance customer service with up-to-date bus schedules and seat availability.
        - **Market Analysis:** Gain insights into travel trends and consumer preferences.
        - **Customer Experience:** Offer tailored travel options and improved services based on data insights.
        - **Competitive Intelligence:** Compare service offerings and pricing with competitors for strategic advantage.
        
        ## Project Approach
        - **Data Extraction:** Use Selenium to scrape data from Redbus.
        - **Data Storage:** Store the data in a SQL database.
        - **Interactive Dashboard:** Visualize and filter the data using a Streamlit application.
        - **Data Analysis:** Provide actionable insights through SQL queries in the Streamlit app.
        
        ## Expected Outcomes
        - Scrape data for multiple state transport services and private buses from Redbus.
        - Organize the data in a SQL database.
        - Build a user-friendly Streamlit app for data filtering and analysis.
        
        ## Skills Acquired
        - Web Scraping with Selenium
        - Data Management with SQL
        - Interactive Data Visualization using Streamlit
        - Python Programming for Data Analysis
    """, unsafe_allow_html=True)

# Render Data Dashboard Content
def render_data_dashboard(engine):
    st.title("🚌 Redbus Data Dashboard")

    # Load data
    data = load_data(engine)

    # Sidebar for filters
    st.sidebar.header("🔍 Filters")

    # State name dropdown
    states = data['state'].unique()
    selected_state = st.sidebar.selectbox("Select State", options=["All"] + list(states))

    # Filter bus names based on selected state
    if selected_state == "All":
        bus_names = data['busname'].unique()
    else:
        bus_names = data[data['state'] == selected_state]['busname'].unique()
    selected_bus_name = st.sidebar.selectbox("Select Bus Name", options=["All"] + list(bus_names))

    # Filter bustype dropdown
    bustypes = data['bustype'].unique()
    selected_bustype = st.sidebar.selectbox("Select Bus Type", options=["All"] + list(bustypes))

    # Route Name filter, dependent on the selected state
    if selected_state == "All":
        route_names = data['route'].unique()
    else:
        route_names = data[data['state'] == selected_state]['route'].unique()
    selected_route_name = st.sidebar.selectbox("Select Route Name", options=["All"] + list(route_names))

    # Price slider
    min_price, max_price = float(data['price'].min()), float(data['price'].max())
    price_range = st.sidebar.slider("Select Price Range", min_value=min_price, max_value=max_price, value=(min_price, max_price))

    # Rating slider
    min_rating, max_rating = float(data['star_rating'].min()), float(data['star_rating'].max())
    rating_range = st.sidebar.slider("Select Star Rating Range", min_value=min_rating, max_value=max_rating, value=(min_rating, max_rating))

    # Apply filters to the data
    filtered_data = data.copy()
    if selected_state != "All":
        filtered_data = filtered_data[filtered_data['state'] == selected_state]
    if selected_bus_name != "All":
        filtered_data = filtered_data[filtered_data['busname'] == selected_bus_name]
    if selected_bustype != "All":
        filtered_data = filtered_data[filtered_data['bustype'] == selected_bustype]
    if selected_route_name != "All":
        filtered_data = filtered_data[filtered_data['route'] == selected_route_name]
    filtered_data = filtered_data[(filtered_data['price'] >= price_range[0]) & (filtered_data['price'] <= price_range[1])]
    filtered_data = filtered_data[(filtered_data['star_rating'] >= rating_range[0]) & (filtered_data['star_rating'] <= rating_range[1])]

    # Show the filtered data
    if filtered_data.empty:
        st.write("No data found for the selected filters.")
    else:
        st.dataframe(filtered_data)

        # Download button
        st.download_button(
            label="Download Data as CSV",
            data=filtered_data.to_csv(index=False),
            file_name='filtered_redbus_data.csv',
            mime='text/csv'
        )

# MAIN FUNCTION
def main():
    page = render_sidebar()
    
    if page == "Home":
        render_home_page()
    elif page == "Data Dashboard":
        render_data_dashboard(engine)

if __name__ == "__main__":
    main()
