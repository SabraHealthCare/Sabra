import pickle
from pathlib import Path
import pandas as pd  
import streamlit as st  

import streamlit_authenticator as stauth

# --- USER AUTHENTICATION ---

usernames = ["pparker", "rmiller"]
names = ["Peter Parker", "Rebecca Miller"]
passwords = ["abc123", "def456"]


# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

credentials = {"usernames":{}}

hashed_passwords = stauth.Hasher(passwords).generate()
for uname,name,pwd in zip(usernames,names,passwords):
    user_dict = {"name": name, "password": pwd}
    credentials["usernames"].update({uname: user_dict})
        
authenticator = stauth.Authenticate(credentials, "cokkie_name", "random_key", cookie_expiry_days=30)
name, authentication_status, username = authenticator.login("Login", "main")
st.write(name, authentication_status, username)
if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    placeholder.empty()
    st.write("got")

   
    # ---- SIDEBAR ----
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    st.sidebar.header("Please Filter Here:")
    city = st.sidebar.multiselect(
        "Select the City:",
        options=df["City"].unique(),
        default=df["City"].unique()
    )

    customer_type = st.sidebar.multiselect(
        "Select the Customer Type:",
        options=df["Customer_type"].unique(),
        default=df["Customer_type"].unique(),
    )

    gender = st.sidebar.multiselect(
        "Select the Gender:",
        options=df["Gender"].unique(),
        default=df["Gender"].unique()
    )

    df_selection = df.query(
        "City == @city & Customer_type ==@customer_type & Gender == @gender"
    )

    # ---- MAINPAGE ----
    st.title(":bar_chart: Sales Dashboard")
    st.markdown("##")

    # TOP KPI's
    total_sales = int(df_selection["Total"].sum())
    average_rating = round(df_selection["Rating"].mean(), 1)
    star_rating = ":star:" * int(round(average_rating, 0))
    average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader("Total Sales:")
        st.subheader(f"US $ {total_sales:,}")
    with middle_column:
        st.subheader("Average Rating:")
        st.subheader(f"{average_rating} {star_rating}")
    with right_column:
        st.subheader("Average Sales Per Transaction:")
        st.subheader(f"US $ {average_sale_by_transaction}")

    st.markdown("""-------------------------------------------------""")
