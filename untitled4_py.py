# -*- coding: utf-8 -*-
"""Untitled4.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N_jORsZVUbqWgeD_a-GojAcup6v-_C8u
"""

pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile our_application.py
# import streamlit as st
# st.write("Hello")



! wget -q -O - ipv4.icanhazip.com

! streamlit run our_application.py & npx localtunnel --port 8501

