import streamlit as st
import pandas as pd
import requests
from linearmodels.panel import PanelOLS

st.set_page_config(page_title="EU Macroeconomic Panel Dashboard", layout="wide")

st.title("🇪🇺 European Macroeconomic Panel Data Dashboard")
st.markdown("### Applied Econometrics & Panel Data Analysis (Fixed Effects Model)")

# Sidebar for user inputs
st.sidebar.header("Dashboard Controls")
indicator = st.sidebar.selectbox(
    "Select Macroeconomic Indicator",
    options=["NY.GDP.MKTP.KD.ZG", "FP.CPI.TOTL.ZG"],
    format_func=lambda x: "GDP Growth (annual %)" if x == "NY.GDP.MKTP.KD.ZG" else "Inflation, consumer prices (annual %)"
)

# Fetch data from World Bank API for major EU economies
countries = {"Italy": "ITA", "Germany": "DEU", "France": "FRA", "Spain": "ESP"}
data_frames = []

@st.cache_data
def fetch_wb_data(ind_code):
    all_data = []
    for name, code in countries.items():
        url = f"http://api.worldbank.org/v2/country/{code}/indicator/{ind_code}?date=2010:2023&format=json"
        response = requests.get(url)
        if response.status_code == 200:
            res_json = response.json()
            if len(res_json) > 1 and res_json[1]:
                for item in res_json[1]:
                    if item['value'] is not None:
                        all_data.append({
                            'Country': name,
                            'Year': int(item['date']),
                            'Value': item['value']
                        })
    return pd.DataFrame(all_data)

df = fetch_wb_data(indicator)

if not df.empty:
    st.success("Data successfully fetched from World Bank API!")
    
    # Display raw data preview
    st.subheader("Raw Panel Data Preview")
    st.dataframe(df.head(10))

    # Set Multi-Index for Panel Data
    panel_df = df.set_index(['Country', 'Year'])

    st.subheader("Descriptive Statistics")
    st.write(panel_df.describe())

    # Simple Panel Regression Example
    st.subheader("Panel Data Econometric Model (Fixed Effects)")
    try:
        # Creating a dummy regressor for demonstration (e.g., time trend)
        panel_df['Trend'] = panel_df.index.get_level_values('Year') - 2009
        
        # Dependent variable: Value, Independent variable: Trend
        model = PanelOLS(panel_df['Value'], panel_df['Trend'], entity_effects=True, time_effects=True)
        results = model.fit()
        
        st.text(results.summary)
    except Exception as e:
        st.warning(f"Could not run regression with current selection: {e}")

else:
    st.error("Failed to fetch data from the API. Please check your internet connection.")
