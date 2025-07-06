import streamlit as st
from streamlit import session_state as state
from Augment_Generation import run_query
st.subheader("Customer Complaint Answering Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message  in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role":"user" , "content" : prompt })
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        st.markdown("Processing your request...")
        stream = run_query(prompt)
        response = st.write(stream)
    st.session_state.messages.append({"role":"assistant", "content": response})
