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
furn = st.selectbox("The house is : ",houses['furniture'].unique())
st.write(furn)
c = st.color_picker('Pick A Color', '#00f900')

plot_type=st.radio("select the plot type",['scatter','line','area'])
if plot_type == 'scatter':
  pl = alt.Chart(houses[houses['furniture']==furn]).mark_circle(color=c).encode(
    x = 'rooms',
    y ='bathroom',
    tooltip = ['rooms','bathroom']
).interactive()
else:
  if plot_type == 'line':
    pl = alt.Chart(houses[houses['furniture']==furn]).mark_bar(color=c).encode(
      x = 'rooms',
      y ='bathroom',
      tooltip = ['rooms','bathroom']
      
    ).interactive()
  else:
     #pl=pd.DataFrame(houses[['rooms','bathroom']])
     #st.area_chart(pl,use_container_width=True)
     pl=alt.Chart(houses[houses['furniture']==furn]).mark_area(opacity=0.3,color=c).encode(
     x="rooms:T",
     y=alt.Y("bathroom:Q", stack=None)
     
     )

st.altair_chart(pl)

st.subheader('Pie cahrt shows the total cost with tax in each city')


pll=alt.Chart(houses).mark_arc().encode(
    theta=alt.Theta(field="total (R$)", type="quantitative"),
    color=alt.Color(field="city", type="nominal"),
)

st.altair_chart(pll)




