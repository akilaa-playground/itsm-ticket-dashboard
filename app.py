import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/tickets.csv", parse_dates=["CreatedDate"])

st.set_page_config(page_title="ITSM Dashboard", layout="wide")
st.title("📊 ITSM Ticket Dashboard")

# Filters
st.sidebar.header("Filter Tickets")
ticket_type = st.sidebar.multiselect("Type", df["Type"].unique(), default=df["Type"].unique())
status = st.sidebar.multiselect("Status", df["Status"].unique(), default=df["Status"].unique())
priority = st.sidebar.multiselect("Priority", df["Priority"].unique(), default=df["Priority"].unique())

filtered_df = df[
    (df["Type"].isin(ticket_type)) &
    (df["Status"].isin(status)) &
    (df["Priority"].isin(priority))
]

st.markdown(f"### Showing {len(filtered_df)} tickets")

# Ticket count by type
st.subheader("Ticket Count by Type")
type_counts = filtered_df["Type"].value_counts()
st.bar_chart(type_counts)

# Tickets over time
st.subheader("Ticket Trend Over Time")
df_by_date = filtered_df.groupby("CreatedDate").size()
st.line_chart(df_by_date)

# Pie chart of statuses
st.subheader("Ticket Status Distribution")
status_counts = filtered_df["Status"].value_counts()

fig, ax = plt.subplots()
ax.pie(status_counts, labels=status_counts.index, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)
