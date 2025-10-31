# 📊 Superstore Sales Data Analysis Project

This project provides a comprehensive analysis of the "Superstore Sales" dataset using Python and its specialized libraries. The goal of the analysis is to uncover patterns, identify Key Performance Indicators (KPIs), and present visual insights to understand sales performance.

-----

## 🚀 Project Overview

This analysis includes the following key steps:

1.  **Data Loading:** Importing the dataset.
2.  **Data Cleaning:** Handling missing values, removing duplicates, and correcting data types.
3.  **Feature Engineering:** Deriving new columns (like Year and Month) from date columns.
4.  **Exploratory Data Analysis (EDA):** Calculating key KPIs, such as:
      * Total Sales
      * Total Orders
      * Total Customers
      * Average Order Value (AOV)
5.  **Data Visualization:** Creating plots to understand trends and relationships between variables.
6.  **Exporting Results:** Saving the clean data to a new CSV file.

-----

## 🛠️ Tools and Technologies Used

  * **Python 3.x**
  * **Pandas:** For data manipulation and analysis.
  * **NumPy:** For numerical operations.
  * **Matplotlib:** For basic data visualizations.
  * **Seaborn:** For advanced statistical visualizations.
  * **Jupyter Notebook / iPython:** As an interactive environment for analysis (as indicated by the use of `display()` and `%matplotlib inline`).

-----

## 📈 Key Analyses and Insights

Several KPIs and visualizations were generated:

### 1\. Key Performance Indicators (KPIs)

  * **Total Sales**
  * **Total Orders**
  * **Total Customers**
  * **Average Order Value (AOV)**

### 2\. Visualizations

  * **Sales by Region:** A Bar Plot showing sales performance in each geographical region.
  * **Sales by Category:** A Bar Plot to identify the best-selling categories.
  * **Monthly Sales Trend:** A Line Plot to track sales throughout the year and identify seasonality.
  * **Correlation Heatmap:** To examine the relationship between numerical variables (like Sales and Discount).
  * **Sales by Category and Region:** A Grouped Bar Plot to analyze the performance of categories within each region.

-----

## 📂 Project Outputs

  * `Superstore_Sales.py`: The Python source code for the analysis.
  * `Superstore_Sales_cleaned.csv`: The cleaned dataset, ready for use in other tools (like Power BI or Tableau) after all cleaning and feature engineering steps have been applied.

-----

## ⚙️ How to Run the Project

1.  Clone this repository:
    ```bash
    git clone [Your_Repository_Link]
    ```
2.  Install the required libraries:
    ```bash
    pip install pandas numpy matplotlib seaborn
    ```
3.  Ensure the `Superstore_Sales.csv` file is in the same project directory.
4.  Run the code. It is recommended to use an environment that supports Jupyter (like Jupyter Notebook, VS Code, or Google Colab) to see the outputs and visualizations interactively.



