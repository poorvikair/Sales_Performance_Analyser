import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Sales Performance Dashboard",
    page_icon="📊",
    layout="wide",
)

# Page styling
st.markdown(
    """
    <style>
        .main {
            background-color: #f5f7fb;
        }

        h1, h2, h3 {
            color: #172033;
        }

        [data-testid="stMetric"] {
            background-color: white;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 18px;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.06);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sales data
sales_data = {
    "Rep": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "Region": ["North", "South", "North", "East", "South", "East"],
    "Sales": [87000, 64000, 92000, 78000, 55000, 101000],
    "Quota": [81000, 70000, 85000, 80000, 60000, 95000],
}

sales_df = pd.DataFrame(sales_data)
sales_df["Achievement"] = (
    sales_df["Sales"] / sales_df["Quota"] * 100
).round(1)
sales_df["Quota Status"] = sales_df.apply(
    lambda row: "Met quota" if row["Sales"] >= row["Quota"] else "Below quota",
    axis=1,
)

# Sidebar filters
st.sidebar.header("Filters")
selected_regions = st.sidebar.multiselect(
    "Select region",
    options=sorted(sales_df["Region"].unique()),
    default=sorted(sales_df["Region"].unique()),
)

filtered_df = sales_df[sales_df["Region"].isin(selected_regions)]

# Dashboard header
st.title("Sales Performance Dashboard")
st.write("Track representative performance, quota attainment, and regional sales.")

if filtered_df.empty:
    st.warning("Select at least one region to view the dashboard.")
    st.stop()

# Key metrics
total_sales = filtered_df["Sales"].sum()
average_sales = filtered_df["Sales"].mean()
top_performer = filtered_df.loc[filtered_df["Sales"].idxmax(), "Rep"]
met_quota_count = (filtered_df["Sales"] >= filtered_df["Quota"]).sum()
quota_rate = met_quota_count / len(filtered_df) * 100

metric_columns = st.columns(4)
metric_columns[0].metric("Total sales", f"${total_sales:,.0f}")
metric_columns[1].metric("Average sales", f"${average_sales:,.0f}")
metric_columns[2].metric("Top performer", top_performer)
metric_columns[3].metric("Quota attainment", f"{quota_rate:.1f}%")

st.divider()

# Charts
left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Sales by representative")
    representative_sales = filtered_df.set_index("Rep")["Sales"].sort_values(
        ascending=False
    )
    st.bar_chart(representative_sales, color="#2563eb")

with right_column:
    st.subheader("Sales by region")
    regional_sales = filtered_df.groupby("Region")["Sales"].sum().sort_values(
        ascending=False
    )
    st.bar_chart(regional_sales, color="#14b8a6")

# Performance table
st.subheader("Representative performance")
st.dataframe(
    filtered_df[
        ["Rep", "Region", "Sales", "Quota", "Achievement", "Quota Status"]
    ].sort_values("Sales", ascending=False),
    width="stretch",
    hide_index=True,
    column_config={
        "Sales": st.column_config.NumberColumn("Sales", format="$%d"),
        "Quota": st.column_config.NumberColumn("Quota", format="$%d"),
        "Achievement": st.column_config.NumberColumn(
            "Achievement", format="%.1f%%"
        ),
    },
)

# Download button
csv_data = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Download report as CSV",
    data=csv_data,
    file_name="sales_report.csv",
    mime="text/csv",
)
