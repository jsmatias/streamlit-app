import streamlit as st
import numpy as np
import pandas as pd
# from local.sidebar import *
from local import home, page, analysis
# import local.page as page
st.set_page_config(layout="wide")


st.image('images/nav-icn.png', width=200)
PAGES = {
    "Home": home,
    "Data": page,
    "Analysis": analysis
}
st.sidebar.image('images/nav-icn.png', width=100)
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
# st.sidebar.selectbox('Select', [1,2,3])
page = PAGES[selection]
page.app()

# """
# ## Standardization is a priority.
# """

# st.line_chart(df[['rho', 'mua']])

# state = st.button('Show', key='b1')
# placeholder = st.empty()
# if st.checkbox("Show data"):
#     st.table(df[['phantom', 'rho', 'mua', 'musp', 'n1', 'n2']])
# else: placeholder = st.empty()