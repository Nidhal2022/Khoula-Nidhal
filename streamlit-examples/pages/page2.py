from datetime import datetime
import streamlit as st
import pandas as pd
import plotly as px
import plotly as go
import seaborn as sns


houses = pd.read_csv('/content/houses.csv')
st.title('houses Visualization')

def plot():


    
    houses=pd.read_csv('/content/houses.csv')

    clist = houses["city"].unique().tolist()
    countries = st.multiselect("Select country", clist)
    st.header("You selected: {}".format(", ".join(countries)))

    dfs = {country: houses[houses["city"] == country] for country in countries}
    
    fig = go.Figure()
    for country, houses in dfs.items():
        fig = fig.add_trace(go.Bar(x=houses["rooms"], y=houses["rent amount (R$)"], name=country))

    st.plotly_chart(fig)

    ax = sns.regplot(houses['fire insurance (R$)'],houses['rent amount (R$)']).get_figure()

    st.pyplot(ax)


plot()



