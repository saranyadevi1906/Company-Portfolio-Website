import streamlit as st
import pandas

st.set_page_config(layout = "wide")
st.title("The Best Company")

content = """ This is the best company. Reason being Work-Life balance. Employee well-being is our motto.
We provide various opportunities to our employees for both personal and career growth.
Our company offers lucrative packages and various perks.  """
st.write(content)

st.subheader("Our Team")

col1, col2, col3 = st.columns([4,4,4])

data = pandas.read_csv("data.csv")

with col1:
    for index, info in data[:4].iterrows():
        name = info["first name"] + " " +info["last name"]
        st.subheader(name.title())
        st.write(info["role"])
        st.image("images/" + info["image"])

with col2:
    for index, info in data[4:8].iterrows():
        name = info["first name"] + " " +info["last name"]
        st.subheader(name.title())
        st.write(info["role"])
        st.image("images/" + info["image"])

with col3:
    for index, info in data[8:].iterrows():
        name = info["first name"] + " " +info["last name"]
        st.subheader(name.title())
        st.write(info["role"])
        st.image("images/" + info["image"])


