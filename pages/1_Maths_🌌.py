import langc as lch
import streamlit as st

st.title("LC Maths HL")

## "inequalities", "discriminants", "calculus"

eqs = st.sidebar.selectbox("Pick a topic", (" ", "Algebra 1", "Algebra 2", "Algebra 3"))


if eqs == " ":
    topic = False
    st.write("""
*"The only way to learn mathematics is to do mathematics."* — Paul Halmos
""")
    st.write("Select your level (you can make the lessons easier or harder)")
    x = st.slider("x", key="level")

    st.text_input("Your name", key="name")

    # You can access the value at any point with:
    st.session_state.name
    st.session_state.level

    

if eqs == "Algebra 1":
    st.markdown("""
                The key topics are: 
                \n- Expressions in algebra (e.g. what is the variable and coefficient in 5x?) 
                \n- Notation ()
                """)

if eqs == "Algebra 1":
    topic = st.sidebar.text_area(label="What do you want to know", max_chars=40)

if eqs == "Algebra 2":
    topic = st.sidebar.text_area(label="What do you want to know", max_chars=40)

if eqs == "Algebra 3":
    topic = st.sidebar.text_area(label="What would you like to know about?", 
                                 placeholder = "for example, what is an inequality?",
                                 max_chars=40)

if topic:
    response = lch.define_maths_concept(topic)
    st.markdown(response["topic"])


