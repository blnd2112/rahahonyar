import streamlit as st
from PIL import Image
from io import BytesIO


import base64
import time

import os
from datetime import datetime

st.set_page_config(page_title="balla form", initial_sidebar_state="expanded", layout="wide")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
footer {
    visibility: hidden;
}
footer:after {
    content:'Made by Honiyar & Raha';
    visibility: visible;
    display: block;
    position: relative;
    #background-color: red;
    padding: 5px;
    top: 2px;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
with st.container():
    cal1, cal2, cal3, cal4 = st.columns([7, 5, 5, 5])
    with cal1:
        def add_bg_from_local(image_file):
            with open(image_file, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url('data:image/png;base64,{encoded_string}');
                    background-size: cover;
                    background-repeat: no-repeat;
                    background-position: center;

                }}
                </style>
                """,
                unsafe_allow_html=True
            )



        st.markdown("""
                <style>
                .big-font {
                    font-size: 60px !important;
                    color: white !important;
                    font-weight: bold !important;
                }
                </style>
                """, unsafe_allow_html=True)

        st.markdown('<p class="big-font">Honiyar & Raha form</p>', unsafe_allow_html=True)

        with cal4:
            st.write(" ")
        with cal2,cal3:
            st.write(" ")
with st.container():
    col1, col2, col3 = st.columns([5, 5, 4])
    with col1:



        name = st.text_input("First Name")





    with col2:

        last = st.text_input("Last Name")

    e = st.text_input("Email address")

with st.container():
    col1, col2, col3 = st.columns([5, 5, 4])
    with col1:



        name = st.text_input("Password")
        with st.container():
            st.write("gender")
            ccol1, ccol2 = st.columns([5, 5])
            with ccol1:

                st.checkbox("Male")
            with ccol2:
                st.checkbox("Female")

        note_key = f"note_{name}"
        note_placeholder = st.empty()
        note = note_placeholder.selectbox(
            "Source of Income",
            options=[
                'Employed'
            ],
            key=note_key)
        st.file_uploader("Upload profile picture")






    with col2:

        last = st.text_input("Confirm Password")
        st.write("Hobbies")
        with st.container():
            cccol1, cccol2,cool3, col4 = st.columns([5, 5, 5, 5])
            with cccol1:

                st.checkbox("Music")
            with cccol2:
                st.checkbox("Sport")
            with cool3:
                st.checkbox("Travel")
            with col4:
                st.checkbox("Movies")

        amount = st.slider("Income", min_value=1, max_value=20)
        st.text_input("age")
    st.text_input("Bio")
    st.button("Create")
