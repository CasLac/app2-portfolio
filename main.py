import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Myselfman")
    content = """
    Myselfman is a computer engineer with over 40 years of experience and is currently a IT consultant.
He is an experienced and qualified professional with extensive knowledge in various technologies and business areas.
With a consistent track record, he started his career as an analyst and programmer and has been evolving to more comprehensive projects over time.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python, Fell free to contact me!
"""

st.write(content2)