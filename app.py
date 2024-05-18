import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go

# Load the database helper
db = DB()

# Set page configuration
st.set_page_config(
    page_title="Flights Analytics",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar title and menu options
st.sidebar.title('🛫 Flights Analytics')
user_option = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1, col2 = st.columns(2)
    city = db.fetch_city_names()

    with col1:
        
        source = st.selectbox('Source', sorted(city))

    with col2:
        destination = st.selectbox('Destination', sorted(city))

    if st.button('Search'):
        result = db.fetch_all_flights(source, destination)
        st.dataframe(result)

elif user_option == 'Analytics':
    
    try:
        airline, frequency = db.fetch_airline_frequency()
        fig_airline = go.Figure(
            go.Pie(
                labels=airline,
                values=frequency,
                hoverinfo='label+percent',
                textinfo='value'
            )
        )
        st.header("Airline Distribution",  divider=True)
        st.plotly_chart(fig_airline, use_container_width=True)

    except Exception as e:
        st.error(f"Error fetching airline frequency: {str(e)}")

    try:
        city, frequency1 = db.busy_airport()
        fig_busy_airport = go.Figure(
            go.Bar(
                x=city,
                y=frequency1,
                hoverinfo='x+y',
                text=city,
                textposition='auto'
            )
        )
        st.header("Busy Airports",  divider=True)
        st.plotly_chart(fig_busy_airport, use_container_width=True)
    except Exception as e:
        st.error(f"Error fetching busy airports: {str(e)}")

    try:
        date, frequency2 = db.daily_frequency()
        fig_daily_frequency = go.Figure(
            go.Line(
                x=date,
                y=frequency2,
                hoverinfo='x+y',
                mode='lines+markers'
            )
        )
        st.header("Daily Flight Frequency",  divider=True)
        st.plotly_chart(fig_daily_frequency, use_container_width=True)
    except Exception as e:
        st.error(f"Error fetching daily flight frequency: {str(e)}")

else:
    st.title('🛫 Flight Insights Dashboard')
    st.markdown(
        """
        Welcome to the Flights Analytics Dashboard! 

        This dashboard provides insights and analytics about flight data. Use the sidebar to navigate between different sections:

        - **Check Flights:** Search for flights between different cities.
        - **Analytics:** Explore analytics including airline distribution, busy airports, and daily flight frequency.

        Start exploring now by selecting an option from the sidebar!
        """
    )

    