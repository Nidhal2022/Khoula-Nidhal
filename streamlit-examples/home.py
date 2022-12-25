
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import matplotlib as plt
import seaborn as sns

houses = pd.read_csv('/content/houses.csv')
houses=houses.dropna()
houses=houses[houses['area']<400]
houses=houses[houses['total (R$)']<8000]


st.title('houses Visualization 🏡')
st.header(' Background of the Dataset ')







st.subheader(' These are :red[columns] of houses for rent in Brazil Dataset ')

import graphviz as graphviz
graph = graphviz.Digraph()

for i in houses.columns[0:8]:
  graph.edge('Houses data',i)

graph.edge('Houses data',houses.columns[12])
for i in houses.columns[11:8:-1]:
  graph.edge(houses.columns[12],i)
  

  

st.graphviz_chart(graph)

def get_correlated(cor):

    correlated =set()

    for i in cor.columns:

        for j in cor.columns:

            if cor[i][j]>0.7 or cor[i][j]>-0.7 and i!=j:

                correlated.add(i)

                correlated.add(j)

    print("The Correlated columns: {}".format(list(correlated)))

    return correlated

st.subheader(' _correlation_ of columns 📊')


def categorize(col):

    numerical,category=[],[]

    for i in col:

        if houses[i].dtype ==object:

            category.append(i)

        else:

            numerical.append(i)

    print("The numerical features {}:".format(numerical))

    print("The categorical features {}:".format(category))

    return category,numerical



category,numerical = categorize(houses.columns)

cor = houses.corr()



correlated = get_correlated(cor)

b = sns.pairplot(houses[correlated])

st.pyplot(b)


import time
@st.cache(suppress_st_warning=True)
def chosen_sample(a, sam):
    st.write("Cache : chosen_sample(", a, ",", sam, ") ")
    time.sleep(2)  # This makes the function take 2s to run
    return a * sam

a = 1
sam = st.slider('How many sample of data do you want 📝?', 0, 100, 7)
res = chosen_sample(a, sam)

st.write('sample of (', res,' )')


st.table(houses.sample(sam))


st.subheader('Findings')

st.write('''1)This is quite interesting the number of rooms does have a great impact in the rent. More rooms, the rent increases...

2)Sao Paulo are mostly accepting pets and mostly all the other cities are also accepting the pets

3)Mostly the house which allows pets are more costly compared to house that doesn't allows pet and there is some relationship between animal acceptance and total rent

4)Non-Furnished homes are more costly and they are highly opted!!!
Sao Paulo is the city with more non-furnitured houses ''')
