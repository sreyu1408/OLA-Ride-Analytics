
import streamlit as st
import pandas as pd

st.set_page_config(page_title="OLA Ride Insights", layout="wide")

st.title("OLA Ride Insights Dashboard")

df = pd.read_csv("OLA_DataSet.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Ride Count by Vehicle Type")
if 'vehicle_type' in df.columns:
    st.bar_chart(df['vehicle_type'].value_counts())

st.subheader("Booking Status Breakdown")
if 'booking_status' in df.columns:
    st.bar_chart(df['booking_status'].value_counts())
# ---------------- POWER BI DASHBOARDS ----------------

st.markdown("---")
st.header("Power BI Dashboard")

st.subheader("Executive Summary")
st.image("powerbi_1.png", use_container_width=True)

st.subheader("Vehicle Analysis")
st.image("powerbi_2.png", use_container_width=True)

st.subheader("Revenue Analysis")
st.image("powerbi_3.png", use_container_width=True)

st.subheader("Cancellation Analysis")
st.image("powerbi_4.png", use_container_width=True)

st.subheader("Rating Analysis")
st.image("powerbi_5.png", use_container_width=True)