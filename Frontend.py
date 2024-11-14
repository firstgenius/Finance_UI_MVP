import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

def main():
    # Set the page layout to wide
    st.set_page_config(layout="wide")

    st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
    }
    .section-title {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
    .app-spacing {
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Sidebar configuration
    with st.sidebar:
        st.markdown("<h2 style='text-align: center;'>User Inputs</h2>", unsafe_allow_html=True)

        # Portfolio size with a clearer title and tooltip
        portfolio_size = st.selectbox(
            "Portfolio size:",
            [10, 15, 20, 25, 30, 40, 50],
            help="Select the number of assets in the portfolio."
        )

        # Date range with a more informative label
        st.date_input("Select in-sample time period:", value=[pd.to_datetime("2019-01-01"), pd.to_datetime("2023-12-31")])
        st.date_input("Select out-of-sample period:", value=[pd.to_datetime("2024-01-01"), pd.to_datetime("2024-07-31")])

        # Estimation model with description
        st.selectbox(
            "Choose estimation model:",
            ["Historical timeseries", "Fama-French 3-factor", "Fama-French 5-factor", "APCA"],
            help="Select the estimation model for asset selection."
        )

        # Weights bounds with tooltips
        st.slider("Min weight:", 0, 20, 3, help="Set the minimum weight of the assets.")
        st.slider("Max weight:", 10, 50, 13, help="Set the maximum weight of the assets.")
        
        # Multi-select comparison benchmarks with descriptions
        st.multiselect(
            "Comparison benchmarks:",
            options=["S&P500 index", "Russell 3000 index", "Dow Jones index", "NASDAQ Composite", "Popular invest funds"],
            default=["S&P500 index"],
            help="Choose benchmark indexes for comparison."
        )

        # Action button with styling
        if st.button("Run", type="primary", use_container_width=True):
            with st.spinner('Processing...'):
                time.sleep(3)
                st.success('Done!')

    # Main content layout
    _, col1, _ = st.columns([1, 3, 1])
    with col1:
        st.markdown("<h1 class='main-title'>Outputs</h1>", unsafe_allow_html=True)

    # Sections with images
    image_titles = ["Asset Selection", "In-sample Efficient Frontiers", "Out-of-sample Cumulative Returns", "Out-of-sample Risk and Reward"]
    image_paths = ["placeholder_images/fig1.png", "placeholder_images/fig2.png", "placeholder_images/fig3.png", "placeholder_images/fig4.png"]

    for title, image_path in zip(image_titles, image_paths):
        _, col1, _ = st.columns([1, 3, 1])
        with col1:
            st.markdown(f"<h2 class='section-title'>{title}</h2>", unsafe_allow_html=True)
        image = Image.open(image_path)
        st.image(image, use_column_width=True)


if __name__ == "__main__":
    main()
