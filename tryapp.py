import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import altair as alt
st.markdown(
    """
# Codanics :tada:
**by Dr Ammar**

---
    """
)
st.markdown("""
<span style="color:#003366;font-size:30px">
Data Science is easy if....
</span> <p>your teacher is Dr Ammar and you enroll in chilla4️⃣0️⃣📅</p>
<p style="color:#003366;font-size:30px;color:white">

Graph viz
Streamlit
 </p>
""",unsafe_allow_html=True)






def color_species(species:str):
    colors={
        "Gentoo":"red",
        "Adelie":"#ece9da ",
        "Chinstrap":"green"
    }
    return f"background-color:{colors[species]}"
penguins = sns.load_dataset("penguins")
st.dataframe(penguins.style.applymap(
    color_species,
    subset=["species"],
    )) 


   
    # altair

penguins = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['Length', 'Width', 'Size'])

c = alt.Chart(penguins).mark_circle().encode(
    x='Length', y='Width', size='Size', color='Size', tooltip=['Length', 'Width', 'Size'])

st.altair_chart(c, use_container_width=True)
#line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
#bar chart
chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)
#area chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)

