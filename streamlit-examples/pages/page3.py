import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import matplotlib as plt

houses = pd.read_csv('https://raw.githubusercontent.com/Nidhal2022/Khoula-Nidhal/main/streamlit-examples/houses.csv')
houses=houses.dropna()
houses=houses[houses['area']<400]
houses=houses[houses['total (R$)']<8000]
st.title('houses Visualization')

chart1 = {
    "mark": "point",
    "encoding": {
        "x": {
            "field": "area",
            "type": "quantitative",
        },
        "y": {
            "field": "rent amount (R$)",
            "type": "quantitative",
        },
        "color": {"field": "furniture", "type": "nominal"},
        "shape": {"field": "furniture", "type": "nominal"},        
    },
}

chart2 = {
    "mark": "point",
    "encoding": {
        "x": {
            "field": "area",
            "type": "quantitative",
        },
        "y": {
            "field": "rent amount (R$)",
            "type": "quantitative",
        },
        "color": {"field": "animal", "type": "nominal"},
        "shape": {"field": "animal", "type": "nominal"},
        "size": {"feild": "city", "type":"nominal"},
    },
}

chart3 = {
    "mark": "point",
    "encoding": {
        "x": {
            "field": "area",
            "type": "quantitative",
        },
        "y": {
            "field": "rent amount (R$)",
            "type": "quantitative",
        },
        "color": {"field": "city", "type": "nominal"},
        "shape": {"field": "city", "type": "nominal"},
        "size": {"feild": "rooms", "type":"quantitative"},

    },
}

need_help = st.expander("Need sompe specifications? 👉")
with need_help:
    st.markdown(
        "the tabs will the show area of the houses and their relation with the cost ( rent amount ) of the houses / the data shown depending on furniture, animal, city"
     )

tab1, tab2, tab3 = st.tabs(["furniture", "animal","city"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.vega_lite_chart(
        houses, chart1, theme="streamlit", use_container_width=True
    )
with tab2:
    st.vega_lite_chart(
        houses, chart2, theme=None, use_container_width=True
    )
with tab3:
    st.vega_lite_chart(
        houses, chart3, theme="streamlit", use_container_width=True
    )

    
