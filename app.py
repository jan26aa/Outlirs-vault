import streamlit as st
import pandas as pd
import json
import os

st.title("outlier vault dashboard")
st.write("This is an interactivw interface to display raw logs and detected security alerts.")

if os.path.exists("raw_logs.csv"):
    st.subheader("Raw Data Logs")
    df_raw = pd.read_csv("raw_logs.csv")
    st.dataframe(df_raw)

    if os.path.exists("alerts.json"):
        st.subheader("Detected Alerts")
        with open("alerts.json", "r") as f:alerts_data = json.load(f)
        if alerts_data:
            st.json(alerts_data)
        else:
            st.info("No alerts found currently.")
    else:
        st.warning("The alerts.json file was not found. Pleas run the analysis script first.")