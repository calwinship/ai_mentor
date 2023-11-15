import langc as lch
import streamlit as st
import numpy as np
import pandas as pd

st.title("Physics")

st.write("""
*"I'm not smart. I just spend longer at problems"* — Einstein
""")
   

map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [52.39, -8.37],
    columns = ['lat', 'lon'])

st.map(map_data)
st.markdown('\n\nCalculus is a branch of mathematics that deals with the study of change. It is used to analyze how a quantity changes over time, and it is used to solve problems in many fields, such as physics, engineering, economics, and medicine. Calculus is used to find the rate of change o')



response = lch.langchain_agent()
st.markdown(response)