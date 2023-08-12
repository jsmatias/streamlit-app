import streamlit as st
import pandas as pd
import local.sidebar as sidebar
import plotly.figure_factory as ff
import numpy as np


def app():
    st.title('Analysis')
    st.write('Fit the curve')

    col1, col2 = st.columns([1, 2])
    col1.button('Fit')
    data = pd.read_csv('data/Contini1997.csv')
    x0 = col1.slider('Min range', 0, 320, 0, 1)
    x1 = col1.slider('Min range', 0, 320, 320, 1)

    # col1.table(data[['rho', 'mua', 'musp']])
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    # Group data together
    hist_data = [x1, x2, x3]
    group_labels = ['Group 1', 'Group 2', 'Group 3']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

    # Plot!
    col2.plotly_chart(fig, use_container_width=True)

    sidebar.app()
    return (None)
