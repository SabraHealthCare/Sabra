import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
conn = st.experimental_connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from users;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.user_name} has a :{row.password}:")

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
#st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

