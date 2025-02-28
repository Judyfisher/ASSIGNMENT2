# Amazon Product Data Analysis

This repository contains an analysis of Amazon product data, focusing on sales, customer engagement, and discount strategies.

## Data Source

The data is sourced from `amazon.csv`, containing information about various Amazon products, including:

* Product names
* Categories
* Ratings
* Review counts
* Prices
* Discounts
* User reviews (if available)

## Analysis Steps

1.  **Data Loading and Cleaning:**
    * Loaded the CSV data into a Pandas DataFrame.
    * Cleaned and transformed the data, including:
        * Handling missing values.
        * Converting data types.
        * Removing non-numeric characters from the discount_percentage column.
        * Removing commas from the rating_count column and converting it to an integer.
2.  **Database Integration:**
    * Created a MySQL database (`ecommerce_db`).
    * Created a table (`amazon_products_table`) mirroring the CSV structure.
    * Loaded the cleaned data into the MySQL table using `pandas.to_sql()`.
3.  **SQL Queries:**
    * Performed various SQL queries to:
        * Retrieve the top 10 most reviewed products.
        * Find the category with the highest average rating.
        * Identify products with discounts greater than 50%.
        * Find the user with the most reviews.
        * List the top 5 best-selling categories.
4.  **Data Visualization:**
    * Created visualizations using Matplotlib and Seaborn, including:
        * Histograms of rating distributions.
        * Scatter plots of discount vs. rating count and discount percentage vs. rating.
        * Bar charts of top 10 highest-rated products.
        * Pie charts of top-selling categories.
        * Heatmaps of correlation between numerical columns.
5.  **Correlation Analysis:**
    * Calculated correlations between discount percentage and rating, and discount amount and rating count.
6.  **Recommendations:**
    * Suggested product categories to prioritize for discounts.
    * Recommended strategies to improve sales and customer engagement.
    * Discussed potential anomalies and patterns found in the data.

## Libraries Used

* Pandas
* SQLAlchemy
* PyMySQL
* Matplotlib
* Seaborn
* re (Regular expressions)

## Key Findings

* "Category X has the highest average rating," "There's a positive correlation between discount and sales in category Y," etc.)

## Recommendations

"Prioritize discounts in high-rated, low-sales categories," "Improve product listing quality," etc.)

## How to Run

1.  Install the required libraries: `pip install pandas sqlalchemy pymysql matplotlib seaborn`
2.  Set up a MySQL database (`ecommerce_db`) and import the `amazon.csv` data.
3.  Run the Jupyter Notebook (`your_notebook_name.ipynb`).

## Author

*Judy Njuku

