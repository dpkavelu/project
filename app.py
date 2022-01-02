import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_1samp

st.write("# Social media data analysis and Hypothesis testing")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)
    # processing
    data_trending_employers = data[data['categoryType'] == "Top Trending Employers"]
    location = data_trending_employers["countryName"].to_numpy()[0]
    data_trending_jobs = data[data['categoryType'] == "Top Trending Jobs"]
    data_trending_skills = data[data['categoryType'] == "Top Trending Skills"]

    st.subheader("Select the trending")
    genre = st.radio(
        "",
        ('Trending Employers', 'Trending Jobs', 'Trending Skills'))

    if genre == 'Trending Employers':
        st.header('Trending Employers of {}'.format(location))
        fig = plt.figure(figsize=(10, 10))
        sns.barplot(y=data_trending_employers['categoryName'],
                    x=data_trending_employers['categoryValue'],)
        st.pyplot(fig)

    if genre == 'Trending Jobs':
        st.header('Trending Jobs of {}'.format(location))
        fig = plt.figure(figsize=(10, 10))
        sns.barplot(y=data_trending_jobs['categoryName'],
                    x=data_trending_jobs['categoryValue'],)
        st.pyplot(fig)

    if genre == 'Trending Skills':
        fig = plt.figure(figsize=(10, 10))
        st.header('Trending Skills of {}'.format(location))
        sns.barplot(
            y=data_trending_skills['categoryName'], x=data_trending_skills['rank'],)
        st.pyplot(fig)

    values = data['categoryValue'].to_numpy()
    st.header("Hypothesis testing")
    st.subheader("Null Hypothesis (H0) : The trending is useful")
    st.subheader("Alternate Hypothesis (H1) : The trending is not useful")
    tset, pval = ttest_1samp(values, 3)

    if pval < 0.05:    # alpha value is 0.05 or 5%
        st.subheader("Result : We are rejecting null hypothesis")
    else:
        st.subheader("Result : We are accepting null hypothesis")
