# Sales Performance Dashboard

A professional, interactive Streamlit dashboard for monitoring sales team performance, quota attainment, and regional sales trends. This project turns a simple sales dataset into a clean business reporting interface that helps users quickly identify top performers, compare team results across regions, and export filtered sales data for reporting or analysis.

## Live Demo

Open the dashboard here:

https://first-small-project-kdbrdgprf96fczntjpezkm.streamlit.app/

## Project Overview

This repository contains a small but complete data analysis and dashboarding project built with Python. It demonstrates how to:

- create a sales dataset in Python
- calculate sales KPIs such as total revenue and quota attainment
- analyze performance by representative and region
- build a clean dashboard using Streamlit
- filter results dynamically based on selected regions
- export filtered results as a CSV file

The application is designed to be easy to understand, easy to run locally, and useful as a starter project for people learning Python, pandas, and Streamlit.

## Features

- Interactive sidebar filters for sales regions
- Summary metrics for:
  - total sales
  - average sales
  - top performer
  - quota attainment rate
- Sales bar chart by representative
- Regional sales chart by area
- Detailed performance table with:
  - representative name
  - region
  - sales value
  - quota value
  - achievement percentage
  - quota status
- CSV download button for filtered sales data
- Responsive dashboard layout with a clean business reporting style

## How the Dashboard Works

The app loads a small sample dataset containing sales representatives, their assigned regions, sales numbers, and quota targets. It then calculates:

- Achievement = (Sales / Quota) * 100
- Quota Status = "Met quota" or "Below quota"
- Total sales and average sales for the selected region(s)
- Top performer by highest sales
- Quota attainment percentage across the filtered dataset

This information is displayed in metric cards, charts, and a performance table. The user can select one or more regions from the sidebar, and the metrics and reports update automatically.

## Repository Structure

- `app.py` — main Streamlit dashboard application
- `sales.py` — sample analysis script using the same sales dataset
- `requirements.txt` — Python dependencies for the project
- `README.md` — project documentation

## Files in Detail

### `app.py`

This is the main application file. It contains:

- Streamlit page configuration
- custom styling for the dashboard
- a sample data dictionary with sales data for multiple reps
- KPI calculations
- region filtering with `st.sidebar.multiselect()`
- chart generation with `st.bar_chart()`
- a table displaying rep performance
- a CSV download button using `st.download_button()`

### `sales.py`

This file contains a script version of the sales analysis logic. It demonstrates how to:

- build a pandas DataFrame from sales data
- compute sales achievement percentages
- identify reps who met quota
- summarize regional sales totals
- find the top performer in each region

It is useful as a quick script-based example before building the dashboard UI.

### `requirements.txt`

This file lists the project dependencies:

- `pandas`
- `streamlit`

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/poorvikair/first-small-project.git
cd first-small-project
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

3. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
python -m streamlit run app.py
```

5. Open the local URL shown in the terminal to view the dashboard in your browser.

## Example Data

The application uses a sample sales dataset with six representatives across four regions:

- Alice — North
- Bob — South
- Charlie — North
- Diana — East
- Eve — South
- Frank — East

Each rep has:

- sales amount
- quota amount
- calculated achievement percentage
- quota met or below quota status

## Technologies Used

- Python
- pandas
- Streamlit

## Use Cases

This project is suitable for:

- learning dashboard creation in Python
- exploring data analysis workflows
- building KPI-style reporting interfaces
- prototyping sales reporting tools
- practicing filtering, aggregation, and charting with pandas and Streamlit

## Future Enhancements

Possible improvements for this project include:

- adding historical monthly sales data
- supporting more regions and sales reps
- integrating real CSV/Excel uploads
- adding trend charts over time
- including more advanced filtering by rep, date, or sales tier
- adding authentication or multi-page dashboard sections

## Summary

The Sales Performance Dashboard is a simple but effective example of how Python, pandas, and Streamlit can be combined to create a useful business dashboard. It demonstrates the full flow from raw data to metrics, charts, filtering, and downloadable reporting, making it a strong beginner-friendly project for anyone interested in data visualization and dashboard development.

## License

This project is a small personal learning project and is intended for educational/demo use.
