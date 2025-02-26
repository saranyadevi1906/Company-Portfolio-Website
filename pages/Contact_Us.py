import streamlit as st
from mail_operation import send_mail
import pandas


#topics = []
#data = pandas.read_csv("topics.csv")
#for index,item in data.iterrows():
#    topics.append(item["topic"])


data = pandas.read_csv("topics.csv")
with st.form(key = "my_form"):
    user_mail = st.text_input("Your Email Address")
    topic = st.selectbox(label = "What topic do you want to discuss?",
                         options = data["topic"])
    print(topic)
    description = st.text_area("text")
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        message = f"""subject:You have received email from {user_mail}\n
                    From:{user_mail}
                    Topic: {topic}
                    {description}
                    """
        send_mail(message)
        st.info("Your email was sent successfully")
