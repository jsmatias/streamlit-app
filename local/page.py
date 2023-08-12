# app2.py
import streamlit as st
import pandas as pd
import local.sidebar as sidebar


def app():
    st.title('Load Data')
    st.write('Load main data and IRF')

    col1, col2 = st.columns(2)
    file1 = col1.file_uploader('Data')
    file2 = col2.file_uploader('IRF')
    data = None
    irf = None
    if file1:
        data = pd.read_csv(file1)
        col1.table(data[['rho', 'mua', 'musp']])

    if file2:
        irf = pd.read_csv(file2)
        col2.table(irf[['rho', 'mua', 'musp']])
    sidebar.app()
    return (data, irf)
