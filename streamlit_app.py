# streamlit_app.py
import streamlit as st
import requests

st.title("VM JD Matcher")

resume = st.text_area("Paste Resume")
jd = st.text_area("Paste Job Description")

if st.button("Match"):
    response = requests.post("https://your-fastapi-url/match", json={"resume": resume, "jd": jd})
    st.write(response.json())
