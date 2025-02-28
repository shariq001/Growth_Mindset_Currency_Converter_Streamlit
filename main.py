import streamlit as st

# Streamlit Page Configuration for SEO
st.set_page_config(
    page_title="Currency Converter | Muhammad Shariq",  # Title shown on the browser tab
    page_icon="💱",  # Emoji as favicon or provide an image URL
    layout="wide",  # Wide layout for better UI
    initial_sidebar_state="expanded"  # Sidebar expanded by default
)

# Font Awesome Icons Link
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    """,
    unsafe_allow_html=True
)

# Page Link Styling

st.markdown(
    """
    <style>
    [data-testid="stPageLink-NavLink"] {
        background-color: #007F73;
        padding: 0px 10px;
        font-weight: bold;
        border-radius: 5px;
        transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
        transition: 0.8s;
    }

    [data-testid="stPageLink-NavLink"]:hover {
        background-color: #000;
        color: #fff !important;
        padding: 0px 35px;
        transition: 0.8s;
        border: 1px solid white;
        border-radius: 5px;
    }
    
     a {
        background-color: #007F73;
        padding: 8px 10px;
        font-weight: bold;
        color: #fff !important;
        text-decoration: none;
        border-radius: 5px;
        transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
        transition: 0.8s;
    }

     a:hover {
        background-color: #000;
        color: #fff !important;
        padding: 8px 35px;
        transition: 0.8s;
        border: 1px solid white;
        border-radius: 5px;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Title

st.markdown("<h1 style='text-align: center; font-size: 40px; font-weight: bold; color: #FFB200'>GIAIC - Growth Mindset Challenge <i class='fa-brands fa-python'></i></h1>", unsafe_allow_html=True)
st.divider() # for a divider to separate sections


# Navigation Options
pages = {
    "Home": "home",
    "Currency Converter": "pages/currency"
}

# Sidebar Navigation
selected_page = st.sidebar.radio("Navigate",  list(pages.keys()))


# Redirect to Selected Page
if selected_page == "Home":
    st.markdown("<h2 style=' font-weight: bold; color: #1ABC9C'>Created By Muhammad Shariq</h2>", unsafe_allow_html=True)

    st.write("This is a challenge assignment of GIAIC Quarter 3 by Sir Zia, completed as part of the learning journey!")
    
    st.page_link("pages/currency.py", label="Navigate to Converter Page")
    
    st.markdown("<h2 style=' font-weight: bold; color: #1ABC9C'>Visit Muhammad Shariq's Personal Blog <i class='fa-solid fa-newspaper'></h2>", unsafe_allow_html=True)
    
    st.markdown(
    """
    <a href="https://my-personal-blog-eta-virid.vercel.app/" target="_blank">
         Read Blogs Here</i>
    </a>
    """,
    unsafe_allow_html=True
    )
    
    st.write("<p style='margin-top: 20px; color: gray'>Dated: 28 | 2 | 2025</p>", unsafe_allow_html=True)
    
    st.divider()



elif selected_page == "Currency Converter":
    st.switch_page("pages/currency.py")
    