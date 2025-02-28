import streamlit as st
import requests

# Set up Streamlit page
st.set_page_config(page_title="Currency Converter", layout="wide")

# Font Awesome Icons Link
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; font-size: 40px; font-weight: bold; color: #FFB200'>GIAIC - Growth Mindset Challenge <i class='fa-brands fa-python'></i></h1>", unsafe_allow_html=True)
st.divider() # for a divider to separate sections

st.markdown("<h2 style=' font-weight: bold; color: #1ABC9C'>Currency Converter | Muhammad Shariq</h2>", unsafe_allow_html=True)

# Defining Currency Symbols
symbols = {
    "USD": "&#36;", "EUR": "&#8364;", "GBP": "&#163;", "PKR": "&#8360;",
    "INR": "&#8377;", "JPY": "&#165;", "CAD": "&#36;"
}

# Layout
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    currency1 = st.selectbox('From Currency:', symbols.keys()) 
    # input for selecting the currency user wants from to change

with col2:
    st.markdown(f"<h1 style='text-align: center;'>{symbols.get(currency1, '')}</h1>", unsafe_allow_html=True)
    # getting the symbol of currency based on the currency1 user choosed earlier

with col3:
    st.markdown("<h3 style='text-align: center;'>To</h3>", unsafe_allow_html=True)
    # A simple text to display (To)

with col5:
    currency2 = st.selectbox("To Currency:", symbols.keys())
    # input for selecting the currency user wants to change with

with col4:
    st.markdown(f"<h1 style='text-align: center;'>{symbols.get(currency2, '')}</h1>", unsafe_allow_html=True)
    # getting the symbol of currency based on the currency2 user choosed

# My Api Key
API_KEY = st.secrets["api"]["key"]


# url for getting the api requests and also the currencies exchange rate
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency1}/{currency2}"


response = requests.get(url).json()
if response["result"] == "success":
    exchange_rate = response["conversion_rate"]
else:
    exchange_rate = None
# Making sure the currencies exchange rates are available and fetch correcltly from the api above.


# Displaying Results
col1, col2 = st.columns(2) # Defining 2 Columns

with col1:
    if exchange_rate:
        st.success(f"1 {currency1} = {currency2} {exchange_rate} ")
    else:
        st.error(f"Exchange rate not available for {currency1} to {currency2}")
    # displaying the exchange rates in a success message box from currency1 to currency2

with col2:
    if exchange_rate:
        st.success(f"1 {currency2} = {currency1} {1/exchange_rate:.6f} ")  # Reverse Conversion
    else:
        st.error(f"Exchange rate not available for {currency2} to {currency1}")
    # displaying the exchange rates in a success message box from currency2 to currency1
        
col1, col2 = st.columns(2)

with col1:
    amount = st.number_input(currency1) # Number input field to get the amount user wants to convert.
   
    
with col2:
    converted = amount*exchange_rate
    st.success(f"Converted Amount: {converted} {currency2}")
    # Displaying the converted amount in a success msg box.


