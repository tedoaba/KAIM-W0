import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data from the xlsx file
def load_data(uploaded_file):
    """
    Load data from an Excel file.

    Args:
        uploaded_file (streamlit.uploaded_file_manager.UploadedFile): The uploaded Excel file.

    Returns:
        pandas.DataFrame: The loaded data.
    """
    try:
        data = pd.read_excel(uploaded_file)
        return data
    except Exception as e:
        st.error("Error loading data: " + str(e))
        return None

def display_data_preview(data):
    """
    Display the first few rows of the data.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.header("Data Preview")
    st.write(data.head())

def display_data_types(data):
    """
    Display the data types of each column.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.header("Data Types")
    st.write(data.dtypes)

def display_summary_statistics(data):
    """
    Display the summary statistics of the data.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.header("Summary Statistics")
    st.write(data.describe())

def display_distribution(data, column_name):
    """
    Display the distribution of a column.

    Args:
        data (pandas.DataFrame): The data to display.
        column_name (str): The name of the column to display.
    """
    st.header(f"Distribution of {column_name}")
    fig = px.bar(data[column_name].value_counts())
    st.plotly_chart(fig, use_container_width=True)

def display_business_unit_sales(data):
    """
    Display the sales by business unit.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.header("Sales by Business Unit")
    business_unit_sales = data.groupby('business_unit')['Jan'].sum().reset_index()
    fig = px.bar(business_unit_sales, x='business_unit', y='Jan')
    st.plotly_chart(fig, use_container_width=True)  

def display_monthly_sales(data):
    """
    Display the monthly sales.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.header("Monthly Sales")
    monthly_sales = data[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']].sum().reset_index()
    monthly_sales.columns = ['Month', 'Sales']
    fig = px.line(monthly_sales, x='Month', y='Sales')
    st.plotly_chart(fig, use_container_width=True)

def eda_page(data):
    """
    Display the exploratory data analysis page.

    Args:
        data (pandas.DataFrame): The data to display.
    """
    st.title("Exploratory Data Analysis")

    display_data_preview(data)

    analysis_options = {
        "Data Types": display_data_types,
        "Summary Statistics": display_summary_statistics,
        "Distribution": display_distribution,
        "Business Unit Sales": display_business_unit_sales,
        "Monthly Sales": display_monthly_sales
    }

    selected_analyses = st.multiselect("Select analyses to perform", list(analysis_options.keys()))

    for analysis in selected_analyses:
        if analysis == "Distribution":
            column_name = st.selectbox("Select column for distribution", data.columns)
            analysis_options[analysis](data, column_name)
        else:
            analysis_options[analysis](data)

def main():
    """
    The main function.
    """
    st.title("EDA Page")
    uploaded_file = st.file_uploader("Choose a file", type=["xlsx"])
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        if data is not None:
            eda_page(data)
    else:
        st.info("Please upload a file to perform EDA")

if __name__ == "__main__":
    main()